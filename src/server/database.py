from os import getenv

from motor.motor_asyncio import AsyncIOMotorClient


class DataBase:
    client: AsyncIOMotorClient = None
    database_uri = getenv("DATABASE_URI")
    users_collection = None
    address_collection = None
    product_collection = None
    order_collection = None
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
    
    db.users_collection = db.client.shopping_cart.users
    db.address_collection = db.client.shopping_cart.address
    db.product_collection = db.client.shopping_cart.products
    db.order_collection = db.client.shopping_cart.orders
    db.carts_collection = db.client.shopping_cart.carts


async def disconnect_db():
    db.client.close()
