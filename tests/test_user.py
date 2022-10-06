from fastapi import FastAPI
from fastapi.testclient import TestClient
from pytest import mark

from src.controllers.routes_user_async import router as client_router
from src.server.database_test import connect_db, disconnect_db, db

app = FastAPI()
app.include_router(client_router, tags=["user"], prefix="/user")


@app.on_event("startup")
async def startup_db_client():
    await connect_db()
    app.database = db


@app.on_event("shutdown")
async def shutdown_db_client():
    await disconnect_db()
    
@mark.asyncio
async def test_create_user():
     with TestClient(app) as client:
        response = client.post(
            "/user/", json={"name": "Bruna", "email": "teste@gmail.com", "password": "265"}
        )
        assert response.status_code == 201

        body = response.json()
        assert body.get("description") == "OK"
        assert body.get("result").get("name") == "Bruna"
        assert body.get("result").get("email") == "teste@gmail.com"
        assert body.get("result").get("password") == "**********"
        assert "_id" in body.get("result")

@mark.asyncio
async def test_get_user_by_email():
    with TestClient(app) as client:
        user = client.post(
            "/user/", json={"name": "Bruna", "email": "teste@gmail.com", "password": "265"}
        )
        
        body_user = user.json().get("result")
        response = client.get(
            "/user/email/teste@gmail.com"
        )
        
        assert response.status_code == 200
        body = response.json()
        assert body.get("result").get("name") == body_user.get("name")
        assert body.get("result").get("email") == body_user.get("email")
        assert body.get("result").get("password") == body_user.get("password")
        
        #assert body.get("result").get(0).get("name")
