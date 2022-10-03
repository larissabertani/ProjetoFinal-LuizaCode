from typing import List

from bson.objectid import ObjectId
from fastapi import APIRouter, Request, Body, status
from fastapi.encoders import jsonable_encoder

import src.rules.address_rules as address_rules
from src.schemas.address import Address, AddressSchema


router = APIRouter()


@router.post("/{user_email}", response_description="create a new address", response_model=List[Address])
async def route_address(user_email: str, request: Request, new_address: List[Address] = Body(...)):
    new_address = list(map(lambda end: jsonable_encoder(end), new_address))
    user_address = await address_rules.create_user_address(request.app.database.address_collection,
                                        request.app.database.users_collection,
                                        user_email, new_address)
    return user_address['addresses']


@router.get("/{user_email}", response_description="get address by user email", response_model=List[Address])
async def route_get_address(user_email: str, request: Request):
    user_address = await address_rules.get_address_by_user(request.app.database.address_collection, user_email)
    return user_address['addresses']


@router.delete("/{email}", response_description="delete a address")
async def route_delete_address(email: str, requests: Request):
    return await address_rules.delete_address(requests.app.database.address_collection, email)