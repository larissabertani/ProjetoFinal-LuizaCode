from fastapi import FastAPI
from fastapi.testclient import TestClient
from pytest import mark

from src.controllers.routes_products_async import router as product_router
from src.server.database_test import connect_db, disconnect_db, db

app = FastAPI()
app.include_router(product_router, tags=["products"], prefix="/products")


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
                "qt_stock": 15
                })
        
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
                                "type_animal": "dog","category": "food", "qt_stock": 15}
        )
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
                                "type_animal": "dog","category": "food", "qt_stock": 15}
        )
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
        
        assert response.status_code == 200
        body = response.json()
        assert body.get("description") == 'Não existe produto com este código!'
        assert body.get("result") is None

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
        
        assert response.status_code == 200
        body = response.json()
        assert body.get("description") == 'Não existe produto com este nome!'
        assert body.get("result") is None

        

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
        

