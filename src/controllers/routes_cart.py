from typing import List

from bson.objectid import ObjectId
from fastapi import APIRouter, Request, Body, status
from fastapi.encoders import jsonable_encoder
from src.models.cart import create_cart

from src.schemas.cart import CartTotalSchema, CartResponse

router = APIRouter()

# Criar novo carrinho
@router.post("", response_description="create a new address", response_model=CartResponse)
async def route_cart(cart: CartTotalSchema):
    response = await create_cart(cart)
    return response