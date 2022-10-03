"""
Regras e ajustes para usuários (clientes)

"""

from typing import List
import src.models.user as user_models
import src.models.address as address_models
from src.schemas.user import UserSchema


async def create_user(users_collection, user):
    db_user = await user_models.get_user_by_email(users_collection, user['email'])
    if db_user:
        return "Já existe um cliente cadastrado com este e-mail!"
    user = await user_models.create_user(users_collection, user)
    if user.inserted_id:
        user = await user_models.get_user(users_collection, user.inserted_id)
        return user
    return "Ocorreu um erro ao inserir o usuário!"
    
    
async def get_user(users_collection, user_id):
    return await user_models.get_user(users_collection, user_id)
    
async def get_users(users_collection, skip, limit):
    users = await user_models.get_users(users_collection, skip, limit)
    if users:
        return users
    return List[UserSchema]
         
async def get_user_by_email(users_collection, email):
    user = await user_models.get_user_by_email(users_collection, email)
    if user:
        return user
    return "Este e-mail não possui cadastro!"
              
async def update_user(users_collection, user_id, user_data):
    return await user_models.update_user(users_collection, user_id, user_data)
                  
async def delete_user(users_collection, address_collection, user_email):
    await address_models.delete_address(address_collection, user_email)
    
    user = await user_models.delete_user(users_collection, user_email)
    if user.deleted_count:
        return "Usuário deletado com sucesso!"
    return "Não há usuário com este email para ser deletado!"