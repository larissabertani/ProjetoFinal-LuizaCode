from typing import List

from bson.objectid import ObjectId
from fastapi import APIRouter, Request, Body, status
from fastapi.encoders import jsonable_encoder
import src.rules.cart_rules as cart_rules

from src.schemas.cart import CartSchema, CartResponse

router = APIRouter()

# Criar novo carrinho
# @router.post("/", response_description="create a new cart", response_model=CartResponse)
# async def route_create_cart(cart: CartSchema, requests: Request):
#     response = await create_cart(requests.app.database.carts_collection, cart)
#     return response

# Adicionar item no carrinho
@router.post("/{user_id}/{product_code}", response_description="create a new cart", response_model=CartResponse)
async def route_create_cart(requests: Request, user_id, product_code: int):
    response = await cart_rules.add_item_cart(requests.app.database.carts_collection, requests.app.database.users_collection, requests.app.database.product_collection, user_id, product_code)
    return await process_cart_response(response)


# Consultar carrinho de compras aberto
@router.get("/{user_id}", response_description="get an open cart", response_model=CartResponse)
async def route_get_cart(requests: Request, user_id):
    response = await cart_rules.get_cart(requests.app.database.carts_collection, user_id)
    return await process_cart_response(response)


# process result
async def process_cart_response(response):
    if type(response) == str:
        return CartResponse(description = response)
    return CartResponse(description = 'OK', result = response)


# deletar carrinho
@router.delete("/{user_email}", response_description="delete a cart")
async def route_delete_cart(user_email: str, requests: Request):
    response = await cart_rules.delete_cart(requests.app.database.carts_collection, user_email)
    return await process_cart_response(response)

