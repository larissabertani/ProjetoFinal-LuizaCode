from os import getenv

from motor.motor_asyncio import AsyncIOMotorClient


class DataBase:
    client: AsyncIOMotorClient = None
    database_uri = getenv("DATABASE_URI")
    users_collection = None
    address_collection = None
    product_collection = None
    order_collection = None
    order_items_collection = None
    carts_collection = None


db = DataBase()


async def connect_db():
    db.client = AsyncIOMotorClient(
        db.database_uri,
        maxPoolSize=10,
        minPoolSize=10,
        tls=True,
        tlsAllowInvalidCertificates=True
    )
    
    db.users_collection = db.client.shopping_cart_test.users
    db.address_collection = db.client.shopping_cart_test.address
    db.product_collection = db.client.shopping_cart_test.products
    db.order_collection = db.client.shopping_cart_test.orders
    db.order_items_collection = db.client.shopping_cart_test.order_items
    db.carts_collection = db.client.shopping_cart_test.carts


async def disconnect_db():
    await db.users_collection.drop()
    await db.address_collection.drop()
    await db.product_collection.drop()
    await db.order_collection.drop()
    await db.order_items_collection.drop()
    await db.carts_collection.drop()  
    db.client.close()
