from urllib import response
from fastapi import APIRouter, Body, Request, status
from fastapi.encoders import jsonable_encoder
from typing import List
from bson.objectid import ObjectId

import src.rules.user_rules as user_rules
from src.schemas.user import UserResponse, UserSchema


router = APIRouter()

# pegar usuarios
@router.get("/", response_model=List[UserSchema])
async def route_get_user(requests: Request):
    return await user_rules.get_users(requests.app.database.users_collection, 0, 2)

# criar um usuário
@router.post("/", response_description="Create an user", response_model=UserResponse)
async def route_create_user(requests: Request, new_user: UserSchema = Body(...)):
    new_user = jsonable_encoder(new_user)
    response = await user_rules.create_user(requests.app.database.users_collection, new_user)
    return await process_user_response(response)

# Retornar um usuário pelo id
@router.get("/{id}", response_description="Get a user by id", response_model=UserResponse)
async def route_get_by_id(id: str, request: Request):
    response = await user_rules.get_user(request.app.database.users_collection, ObjectId(str(id)))
    return await process_user_response(response)

# Retornar um usuário pelo email
@router.get("/email/{email}", response_description="Get a user by email", response_model=UserResponse)
async def route_get_by_email(email: str, request: Request):
    response = await user_rules.get_user_by_email(request.app.database.users_collection, email)
    return await process_user_response(response)

# deletar um usuário
@router.delete("/{email}", response_description="delete a user")
async def route_delete_user(email: str, requests: Request):
    response = await user_rules.delete_user(requests.app.database.users_collection, requests.app.database.address_collection, email)
    return await process_user_response(response)

# process result
async def process_user_response(response):
    if type(response) == str:
        return UserResponse(description = response)
    return UserResponse(description = 'OK', result = response)
