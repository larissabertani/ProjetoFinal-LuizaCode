from fastapi import FastAPI
from fastapi.testclient import TestClient
from pytest import mark

from src.controllers.routes_user_async import router as client_router
from src.server.database_test import connect_db, disconnect_db, db

app = FastAPI()
app.include_router(client_router, tags=["user"], prefix="/user")

headers = {'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c3VhcmlvIjoiTGFyaXNzYSIsInBlcm1pc3NvZXMiOiJhZG1pbiJ9.dfRQXpFuHEA0-E7hH34x6SNzEBGIeHJeIN4BRU8Sr-Hlhh2iVWbrOh273l7FLNScQ-hHhiS-3VvnbnbBENvJw7cv3n2K7CRC9TvrMwnQd3Xej8uiJUyhdMV4nrZf0foJ5BFD-UofVAPDASbFa1a43MTmsxEOSEfJ7WbMEDQBKnuqya-WDdFFPmbin3Ez7MV53Vl-u3DO_S-36Xj6biUDf8d0S5vuruDMSslVAPlHn22EFPh4W8F3Clr4lJwJeWLYOJe52S2rBGJsAux-TN0N8DCZ8fhtRPECmj0yZ9A_xKZLHzvcnY_WKizFCmyaRJpk_m4kt_wPvsjg6R2xe_MG6g'}


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
            "/user/email/teste@gmail.com",
        headers=headers)
        
        assert response.status_code == 200
        body = response.json()
        assert body.get("result").get("name") == body_user.get("name")
        assert body.get("result").get("email") == body_user.get("email")
        assert body.get("result").get("password") == body_user.get("password")
        
        #assert body.get("result").get(0).get("name")

@mark.asyncio
async def test_get_user_by_email_undefined():
    with TestClient(app) as client:
        user = client.post(
            "/user/", json={"name": "Bruna", "email": "teste1@gmail.com", "password": "265"},
            headers=headers)
        
        body_user = user.json().get("result")
        response = client.get(
            "/user/email/teste@gmail.com",
        headers=headers)
        
        assert response.status_code == 404
        body = response.json()
        assert body.get("description") == 'Este e-mail não possui cadastro!'
        assert body.get("result") is None
        
@mark.asyncio
async def test_delete_user_by_email():
    with TestClient(app) as client:
        user = client.post(
            "/user/", json={"name": "Bruna", "email": "teste1@gmail.com", "password": "265"}
        )
        
        body_user = user.json().get("result")
        response = client.delete(
            "/user/teste1@gmail.com"
        )
        assert response.status_code == 200
        body = response.json()
        assert body.get("description") == 'Usuário deletado com sucesso!'
        assert body.get("result") is None
        
        
        
#pegar todos os usuários
@mark.asyncio
async def test_get_all_user():
    with TestClient(app) as client:
        user1 = client.post(
              "/user/", json={"name": "Leandro", "email": "LFE@gmail.com", "password": "123"}
        )
        user2 = client.post(
              "/user/", json={"name": "vitoria", "email": "airotiv@gmail.com", "password": "456"}
        )
        
        body_user1 = user1.json().get("result")
        body_user2 = user2.json().get("result")
        response = client.get(
            "/user/",
        headers=headers)
        
        assert response.status_code == 200
        body = response.json()
        assert body.get("description") == "OK"
        assert body.get("result")[0].get("name") == body_user1.get("name")
        assert body.get("result")[0].get("email") == body_user1.get("email")
        assert body.get("result")[0].get("password") == body_user1.get("password")
        
        assert body.get("result")[1].get("name") == body_user2.get("name")
        assert body.get("result")[1].get("email") == body_user2.get("email")
        assert body.get("result")[1].get("password") == body_user2.get("password")
        
        

        
    
