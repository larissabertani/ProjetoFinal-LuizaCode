
from fastapi import APIRouter, Request
from autentication_jwt import *

import src.rules.cart_rules as cart_rules
from src.schemas.cart import CartResponse

router = APIRouter()


# Adicionar item no carrinho
@router.post("/{user_id}/{product_code}", response_description="add item to cart", response_model=CartResponse)
async def route_create_cart(requests: Request, user_id, product_code: int):
    response = await cart_rules.add_item_cart(requests.app.database.carts_collection, requests.app.database.users_collection, requests.app.database.product_collection, user_id, product_code)
    return await process_cart_response(response)


# Consultar carrinho de compras aberto
@router.get("/{user_id}", response_description="get an open cart", response_model=CartResponse)
async def route_get_cart(requests: Request, user_id, autorizado: bool = Depends(valida_admin)):
    response = await cart_rules.get_cart(requests.app.database.carts_collection, user_id)
    return await process_cart_response(response)


# Remover produto do carrinho de compra
@router.delete("/{user_id}/{product_code}", response_description="remove a product cart", response_model=CartResponse)
async def route_remove_item_cart(requests: Request, user_id, product_code: int):
    response = await cart_rules.delete_product_cart(requests.app.database.carts_collection, user_id, product_code)
    return await process_cart_response(response)


# Deletar carrinho
@router.delete("/{user_email}", response_description="delete a cart")
async def route_delete_cart(user_email: str, requests: Request):
    response = await cart_rules.delete_cart(requests.app.database.carts_collection, user_email)
    return await process_cart_response(response)


# Fechar o carrinho aberto do usuário
@router.post("/{user_email}", response_description="close open cart and create order", response_model=CartResponse)
async def route_close_cart(user_email: str, requests: Request):
    response = await cart_rules.close_cart(requests.app.database.carts_collection, requests.app.database.order_collection, requests.app.database.address_collection, user_email)
    return await process_cart_response(response)


# process result
async def process_cart_response(response):
    if type(response) == str:
        return CartResponse(description = response)
    return CartResponse(description = 'OK', result = response)