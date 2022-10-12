from fastapi import FastAPI
from fastapi.testclient import TestClient
from pytest import mark

from src.controllers.routes_products_async import router as products_router
from src.controllers.routes_user_async import router as client_router
from src.controllers.routes_cart_async import router as cart_router
from src.controllers.routes_order_async import router as order_router
from src.controllers.routes_address_async import router as address_router

from src.server.database_test import connect_db, disconnect_db, db

app = FastAPI()
app.include_router(products_router, tags=["products"], prefix="/products")
app.include_router(client_router, tags=["users"], prefix="/users")
app.include_router(cart_router, tags=["cart"], prefix="/cart")
app.include_router(order_router, tags=["order"], prefix="/order")
app.include_router(address_router, tags=["address"], prefix="/address")


headers = {'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c3VhcmlvIjoiTGFyaXNzYSIsInBlcm1pc3NvZXMiOiJhZG1pbiJ9.dfRQXpFuHEA0-E7hH34x6SNzEBGIeHJeIN4BRU8Sr-Hlhh2iVWbrOh273l7FLNScQ-hHhiS-3VvnbnbBENvJw7cv3n2K7CRC9TvrMwnQd3Xej8uiJUyhdMV4nrZf0foJ5BFD-UofVAPDASbFa1a43MTmsxEOSEfJ7WbMEDQBKnuqya-WDdFFPmbin3Ez7MV53Vl-u3DO_S-36Xj6biUDf8d0S5vuruDMSslVAPlHn22EFPh4W8F3Clr4lJwJeWLYOJe52S2rBGJsAux-TN0N8DCZ8fhtRPECmj0yZ9A_xKZLHzvcnY_WKizFCmyaRJpk_m4kt_wPvsjg6R2xe_MG6g'}

@app.on_event("startup")
async def startup_db_client():
    await connect_db()
    app.database = db


@app.on_event("shutdown")
async def shutdown_db_client():
    await disconnect_db()

#fechar o carrinho e abrir um pedido
@mark.asyncio
async def test_create_order():
     with TestClient(app) as client:
        fake_client = client.post(
            "/users/", json={"name": "Bruna", "email": "teste@gmail.com", "password": "265"}
        )
        body_client = fake_client.json().get("result") 
        new_address = [
        {
            "street": "i know ",
            "number": 10,
            "zipcode": "9999-030",
            "district": "Grass Lands",
            "city": "stark tower",
            "state": "Parallel Universe", 
            "is_delivery": True                     
        }]
      
        fake_address = client.post(
            f"/address/teste@gmail.com", json=new_address
        )
        body_address = fake_address.json()
        
        fake_product = client.post(
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
        body_product = fake_product.json().get("result")
        fake_cart = client.post(
            f"/cart/{body_client.get('_id')}/{body_product.get('code')}"
        )
        body_cart = fake_cart.json().get("result") 
        
        fake_order = client.post(
            f"/cart/{body_client.get('email')}"
        )
        
        body_order = fake_order.json()
        
        assert fake_order.status_code == 200
        assert body_order.get("description") == 'Pedido criado com sucesso!'
        assert body_order.get("result") is None
        
@mark.asyncio
async def test_create_order_invalid_email():
     with TestClient(app) as client:
        fake_client = client.post(
            "/users/", json={"name": "Bruna", "email": "teste@gmail.com", "password": "265"}
        )
        body_client = fake_client.json().get("result") 
        new_address = [
        {
            "street": "i know ",
            "number": 10,
            "zipcode": "9999-030",
            "district": "Grass Lands",
            "city": "stark tower",
            "state": "Parallel Universe", 
            "is_delivery": True                     
        }]
      
        fake_address = client.post(
            f"/address/teste@gmail.com", json=new_address
        )
        body_address = fake_address.json()
        
        fake_product = client.post(
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
        body_product = fake_product.json().get("result")
        fake_cart = client.post(
            f"/cart/{body_client.get('_id')}/{body_product.get('code')}"
        )
        body_cart = fake_cart.json().get("result") 
        
        fake_order = client.post(
            f"/cart/leo22@gmail.com"
        )
        
        body_order = fake_order.json()
        
        assert fake_order.status_code == 404
        assert body_order.get("detail") == 'Este usuário não existe ou não possui carrinho aberto.'
        
#consultando pedido do cliente       
@mark.asyncio
async def test_get_orders():
     with TestClient(app) as client:
        fake_client = client.post(
            "/users/", json={"name": "Bruna", "email": "teste@gmail.com", "password": "265"}
        )
        body_client = fake_client.json().get("result") 
        new_address = [
        {
            "street": "i know ",
            "number": 10,
            "zipcode": "9999-030",
            "district": "Grass Lands",
            "city": "stark tower",
            "state": "Parallel Universe", 
            "is_delivery": True                     
        }]
      
        fake_address = client.post(
            f"/address/teste@gmail.com", json=new_address
        )
        body_address = fake_address.json()
        
        fake_product = client.post(
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
        body_product = fake_product.json().get("result")
        fake_cart = client.post(
            f"/cart/{body_client.get('_id')}/{body_product.get('code')}"
        )
        body_cart = fake_cart.json().get("result") 
        
        fake_order = client.post(
            f"/cart/{body_client.get('email')}"
        )
        
        body_order = fake_order.json()
        
        get_user_orders = client.get(
            f"order/{body_client.get('email')}/skip/0/limit/100"
        )
        
        body_get_user_order = get_user_orders.json()
        
        assert body_get_user_order.get("result")[0].get("user") == body_client
        assert body_get_user_order.get("result")[0].get("address") == body_address.get("result").get("addresses")[0]
        assert get_user_orders.status_code == 200
        
        
        
        # assert fake_cart.status_code == 200
        # assert body_cart.get("user") == body_client
        # assert body_cart.get("cart_items")[0].get("product") == body_product
        # price: float = 0
        # for item in body_cart.get("cart_items"):
        #     price += item['product']['price'] * item['qtd_product']
        # assert body_cart.get("total_price") == price
