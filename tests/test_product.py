from fastapi import FastAPI
from fastapi.testclient import TestClient
from pytest import mark

from src.controllers.routes_products_async import router as product_router
from src.server.database_test import connect_db, disconnect_db, db

app = FastAPI()
app.include_router(product_router, tags=["products"], prefix="/products")

headers = {'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c3VhcmlvIjoiTGFyaXNzYSIsInBlcm1pc3NvZXMiOiJhZG1pbiJ9.dfRQXpFuHEA0-E7hH34x6SNzEBGIeHJeIN4BRU8Sr-Hlhh2iVWbrOh273l7FLNScQ-hHhiS-3VvnbnbBENvJw7cv3n2K7CRC9TvrMwnQd3Xej8uiJUyhdMV4nrZf0foJ5BFD-UofVAPDASbFa1a43MTmsxEOSEfJ7WbMEDQBKnuqya-WDdFFPmbin3Ez7MV53Vl-u3DO_S-36Xj6biUDf8d0S5vuruDMSslVAPlHn22EFPh4W8F3Clr4lJwJeWLYOJe52S2rBGJsAux-TN0N8DCZ8fhtRPECmj0yZ9A_xKZLHzvcnY_WKizFCmyaRJpk_m4kt_wPvsjg6R2xe_MG6g'}

@app.on_event("startup")
async def startup_db_client():
    await connect_db()
    app.database = db


@app.on_event("shutdown")
async def shutdown_db_client():
    await disconnect_db()
    
@mark.asyncio
async def test_create_product():
     with TestClient(app) as client:
        response = client.post(
            "/products/", json={ 
                "name": "Ração Premier",
                "description": "Raças Específicas Lhasa Apso Cães Adultos",
                "price": 124.9,
                "image": "https://static.petz.com.br/fotos/1656091760542.jpg",
                "code": 1243,
                "type_animal": "dog",
                "category": "food",
                "qt_stock": 15},
            headers=headers)
        
        assert response.status_code == 201
        
        body = response.json()
        assert body.get("description") == "OK"
        assert body.get("result").get("name") == "Ração Premier"
        assert body.get("result").get("description") == "Raças Específicas Lhasa Apso Cães Adultos"
        assert body.get("result").get("image") ==  "https://static.petz.com.br/fotos/1656091760542.jpg"
        assert body.get("result").get("code") == 1243
        assert body.get("result").get("type_animal") == "dog"
        assert body.get("result").get("category") == "food"
        assert body.get("result").get("qt_stock") == 15
        assert "_id" in body.get("result")

@mark.asyncio
async def test_get_product_by_name():
    with TestClient(app) as client:
        product = client.post (
            "/products/", json={"name": "Ração Premier", "description": "Raças Específicas Lhasa Apso Cães Adultos",
                                "price": 124.9,"image": "https://static.petz.com.br/fotos/1656091760542.jpg","code": 1243,
                                "type_animal": "dog","category": "food", "qt_stock": 15},
             headers=headers)
        
        body_user = product.json().get("result")
        response = client.get(
            "/products/name/Ração Premier"
        )
        
        assert response.status_code == 200
        body = response.json()
        assert body.get("description") == "OK"
        assert body.get("result").get("name") == "Ração Premier"
        assert body.get("result").get("description") == "Raças Específicas Lhasa Apso Cães Adultos"
        assert body.get("result").get("image") ==  "https://static.petz.com.br/fotos/1656091760542.jpg"
        assert body.get("result").get("code") == 1243
        assert body.get("result").get("type_animal") == "dog"
        assert body.get("result").get("category") == "food"
        assert body.get("result").get("qt_stock") == 15
        assert "_id" in body.get("result")
    
@mark.asyncio
async def test_get_product_by_code():
    with TestClient(app) as client:
        product = client.post (
            "/products/", json={"name": "Ração Premier", "description": "Raças Específicas Lhasa Apso Cães Adultos",
                                "price": 124.9,"image": "https://static.petz.com.br/fotos/1656091760542.jpg","code": 1243,
                                "type_animal": "dog","category": "food", "qt_stock": 15}, 
             headers=headers)
        
        body_user = product.json().get("result")
        response = client.get(
            "/products/code/1243"
        )
        
        assert response.status_code == 200
        body = response.json()
        assert body.get("description") == "OK"
        assert body.get("result").get("name") == "Ração Premier"
        assert body.get("result").get("description") == "Raças Específicas Lhasa Apso Cães Adultos"
        assert body.get("result").get("image") ==  "https://static.petz.com.br/fotos/1656091760542.jpg"
        assert body.get("result").get("code") == 1243
        assert body.get("result").get("type_animal") == "dog"
        assert body.get("result").get("category") == "food"
        assert body.get("result").get("qt_stock") == 15
        assert "_id" in body.get("result")

@mark.asyncio
async def test_get_product_by_code_undefined():
    with TestClient(app) as client:
        product = client.post (
            "/products/", json={"name": "Ração Premier", "description": "Raças Específicas Lhasa Apso Cães Adultos",
                                "price": 124.9,"image": "https://static.petz.com.br/fotos/1656091760542.jpg","code": 1243,
                                "type_animal": "dog","category": "food", "qt_stock": 15}
        )
        body_user = product.json().get("result")
        response = client.get(
            "/products/code/12431"
        )
        
        assert response.status_code == 404
        body = response.json()
        assert body.get("detail") == 'Não existe produto com este código!'
        
@mark.asyncio
async def test_get_product_by_name_undefined():
    with TestClient(app) as client:
        product = client.post (
            "/products/", json={"name": "Ração Premier", "description": "Raças Específicas Lhasa Apso Cães Adultos",
                                "price": 124.9,"image": "https://static.petz.com.br/fotos/1656091760542.jpg","code": 1243,
                                "type_animal": "dog","category": "food", "qt_stock": 15}
        )
        body_user = product.json().get("result")
        response = client.get(
            "/products/name/ração pinscher"
        )
        
        assert response.status_code == 404
        body = response.json()
        assert body.get("detail") == 'Não existe produto com este nome!'
               

@mark.asyncio
async def test_delete_product_by_code():
    with TestClient(app) as client:
        product = client.post(
            "/products/", json={"name": "Ração Premier", "description": "Raças Específicas Lhasa Apso Cães Adultos",
                                "price": 124.9,"image": "https://static.petz.com.br/fotos/1656091760542.jpg","code": 1243,
                                "type_animal": "dog","category": "food", "qt_stock": 15}
        )
        body_user = product.json().get("result")
        response = client.delete(
            "/products/1234"
        )
        

