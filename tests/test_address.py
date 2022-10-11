from fastapi import FastAPI
from fastapi.testclient import TestClient
from pytest import mark

from src.controllers.routes_user_async import router as client_router
from src.controllers.routes_address_async import router as address_router
from src.server.database_test import connect_db, disconnect_db, db

app = FastAPI()
app.include_router(client_router, tags=["user"], prefix="/user")
app.include_router(address_router, tags=["address"], prefix="/address")

headers = {'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c3VhcmlvIjoiTGFyaXNzYSIsInBlcm1pc3NvZXMiOiJhZG1pbiJ9.dfRQXpFuHEA0-E7hH34x6SNzEBGIeHJeIN4BRU8Sr-Hlhh2iVWbrOh273l7FLNScQ-hHhiS-3VvnbnbBENvJw7cv3n2K7CRC9TvrMwnQd3Xej8uiJUyhdMV4nrZf0foJ5BFD-UofVAPDASbFa1a43MTmsxEOSEfJ7WbMEDQBKnuqya-WDdFFPmbin3Ez7MV53Vl-u3DO_S-36Xj6biUDf8d0S5vuruDMSslVAPlHn22EFPh4W8F3Clr4lJwJeWLYOJe52S2rBGJsAux-TN0N8DCZ8fhtRPECmj0yZ9A_xKZLHzvcnY_WKizFCmyaRJpk_m4kt_wPvsjg6R2xe_MG6g'}


@app.on_event("startup")
async def startup_db_client():
    await connect_db()
    app.database = db

@app.on_event("shutdown")
async def shutdown_db_client():
    await disconnect_db()
    
@mark.asyncio
async def test_create_address():
     with TestClient(app) as client:
        fake_client = client.post(
            "/user/", json={"name": "Bruna", "email": "teste@gmail.com", "password": "265"}
        )
        body_user = fake_client.json().get("result")

        address = [{
            "street": "i know ",
            "number": 10,
            "zipcode": "9999-030",
            "district": "Grass Lands",
            "city": "stark tower",
            "state": "Parallel Universe", 
            "is_delivery": True
        }]

        create_user_address = client.post(f"/address/{body_user.get('email')}", json=address)

        body_address = create_user_address.json()

        assert body_address.get('description') == "OK"
        assert body_address.get('result').get('user') == body_user
        assert body_address.get('result').get('addresses') == address

        assert create_user_address.status_code == 200


@mark.asyncio
async def test_get_address():
     with TestClient(app) as client:
        fake_client = client.post(
            "/user/", json={"name": "Bruna", "email": "teste@gmail.com", "password": "265"}
        )
        body_user = fake_client.json()

        address = [{
            "street": "i know ",
            "number": 10,
            "zipcode": "9999-030",
            "district": "Grass Lands",
            "city": "stark tower",
            "state": "Parallel Universe", 
            "is_delivery": True
        }]

        get_user_address = client.get(f"/address/{body_user.get('email')}", json=address, headers = headers)

        body_address = get_user_address.json()

        assert body_address == [{
            "street": "i know ",
            "number": 10,
            "zipcode": "9999-030",
            "district": "Grass Lands",
            "city": "stark tower",
            "state": "Parallel Universe", 
            "is_delivery": True
        }]
    
        assert get_user_address.status_code == 200