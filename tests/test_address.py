from fastapi import FastAPI
from fastapi.testclient import TestClient
from pytest import mark
from unittest import TestCase
from unittest.mock import patch

from main import app

client = TestClient(app)

from src.controllers.routes_address_async import router as address_router
from src.server.database_test import connect_db, disconnect_db, db

app = FastAPI()
app.include_router(address_router, tags=["address"], prefix="/address")

headers = {'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c3VhcmlvIjoiTGFyaXNzYSIsInBlcm1pc3NvZXMiOiJhZG1pbiJ9.dfRQXpFuHEA0-E7hH34x6SNzEBGIeHJeIN4BRU8Sr-Hlhh2iVWbrOh273l7FLNScQ-hHhiS-3VvnbnbBENvJw7cv3n2K7CRC9TvrMwnQd3Xej8uiJUyhdMV4nrZf0foJ5BFD-UofVAPDASbFa1a43MTmsxEOSEfJ7WbMEDQBKnuqya-WDdFFPmbin3Ez7MV53Vl-u3DO_S-36Xj6biUDf8d0S5vuruDMSslVAPlHn22EFPh4W8F3Clr4lJwJeWLYOJe52S2rBGJsAux-TN0N8DCZ8fhtRPECmj0yZ9A_xKZLHzvcnY_WKizFCmyaRJpk_m4kt_wPvsjg6R2xe_MG6g'}

@app.on_event("startup")
async def startup_db_address():
    await connect_db()
    app.database = db

@app.on_event("shutdown")
async def shutdown_db_address():
    await disconnect_db()

fake_db ={
    "users_collection": {"name": "Bruna", "email": "teste@gmail.com", "password": "265"}
}

class ExternoAPIMock:
    def __init__(self, status_code, response=None):
        self.status_code = status_code
        self.response = response

    def json(self):
        return self.response
        
class TestAddress(TestCase):

    @mark.asyncio
    @patch("src.rules.user_rules.create_user")
    async def test_create_address(user_mock):
        #with TestClient(app) as address:
        user_mock.return_value = ExternoAPIMock(status_code=200, response = {"name": "Bruna", "email": "teste@gmail.com", "password": "265"})
        response = client.post(
                "/address/teste@gmail.com", json=[
                {
                    "street": "i know",
                    "number": 10,
                    "zipcode": "9999-030",
                    "district": "Grass Lands",
                    "city": "stark tower",
                    "state": "Parallel Universe", 
                    "is_delivery": True
                }]
            )
        assert response.status_code == 200

        body = response.json()
        assert body.get("description") == "OK"
        assert body.get("result").get("user") == {"name": "Bruna", "email": "teste@gmail.com", "password": "265"}
        assert body.get("result").get("addresses") == [{"street": "i know",
                        "number": 10,
                        "zipcode": "9999-030",
                        "district": "Grass Lands",
                        "city": "stark tower",
                        "state": "Parallel Universe",
                        "is_delivery": True}]


# @mark.asyncio
# async def test_create_address():
#     user ={"name": "Bruna", "email": "teste@gmail.com", "password": "265"}
        
#     with TestClient(app) as client:    
#         response = client.post("/address/teste@gmail.com", json=[
#         {
#         "street": "i know",
#         "number": 10,
#         "zipcode": "9999-030",
#         "district": "Grass Lands",
#         "city": "stark tower",
#         "state": "Parallel Universe", 
#         "is_delivery": True
#         }]
#         )
#         assert response.status_code == 404

#         body = response.json()
#         assert body.get("description") == "OK"
#         assert body.get("result").get("user") == {"name": "Bruna", "email": "teste@gmail.com", "password": "265"}
#         assert body.get("result").get("addresses") == [{"street": "i know", "number": 10, "district": "Grass Lands", "city": "stark tower", "state": "Parallel Universe", "is_delivery": True}]