"""
Regras e ajustes para pedidos (order)

"""

import asyncio
from operator import is_
from src.schemas.order import OrderSchema
import src.models.order as order_models
import src.models.address as address_models
from fastapi.encoders import jsonable_encoder

# Criar pedido
async def create_order(order_collection, address_collection, cart, user_email):
    user_address = await address_models.get_one_address(address_collection, user_email)
    if user_address:
        order = OrderSchema(user = cart['user'], price = cart['total_price'], address = user_address, order_items = cart['cart_items'])
        order = jsonable_encoder(order)
        order = await order_models.create_order(order_collection, order)
        if order.inserted_id:
            return True
    return False

# Consultar pedidos por e-mail
async def get_order_by_email(order_collection, user_email):
    order = await order_models.get_order_by_email(order_collection, user_email, 10)    
    if order:
        return order
    return "Este usuário não possui pedidos!"

# Consultar os produtos e suas quantidades em carrinhos fechados
async def get_product(order_collection, product_code):
    product_qty = await order_models.get_product(order_collection, product_code)
    if product_qty:
        return product_qty
    return "Não há pedidos com este produto!"

# Excluir pedido por id
async def delete_order(order_collection, cart_id):
    order = await order_models.delete_order(order_collection, cart_id)
    if order.deleted_count:        
        return "Pedido deletado com sucesso!"
    return "Erro ao deletar pedido"
    