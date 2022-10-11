"""
Regras e ajustes para usuários (clientes)

"""

from typing import List
import src.models.user as user_models
import src.models.address as address_models
from src.schemas.user import UserSchema
import src.models.cart as cart_models
from fastapi import HTTPException

# Criar usuário
async def create_user(users_collection, user):
    db_user = await user_models.get_user_by_email(users_collection, user['email'])
    if db_user:
        raise HTTPException(status_code=202, detail ="Já existe um cliente cadastrado com este e-mail!")
    user = await user_models.create_user(users_collection, user)
    if user.inserted_id:
        user = await user_models.get_user(users_collection, user.inserted_id)
        return user
    raise HTTPException(status_code=404, detail ="Ocorreu um erro ao inserir o usuário!")
    
# Obter usuário pelo id
async def get_user(users_collection, user_id):
    user = await user_models.get_user(users_collection, user_id)
    if user:
        return user
    raise HTTPException(status_code=404, detail ="Este id não possui cadastro!")
    
# Obter lista de usuários    
async def get_users(users_collection, skip, limit):
    users = await user_models.get_users(users_collection, skip, limit)
    if users:
        return users
    return List[UserSchema]

# Obter usuário pelo e-mail
async def get_user_by_email(users_collection, email):
    user = await user_models.get_user_by_email(users_collection, email)
    if user:
        return user
    raise HTTPException(status_code=404, detail ="Este e-mail não possui cadastro!")

# Atualizar usuário              
async def update_user(users_collection, user_id, user_data):
    user = await user_models.update_user(users_collection, user_id, user_data)
    if user.modified_count:
        return "Usuário alterado com sucesso!"
    raise HTTPException(status_code=404, detail ="Erro ao atualizar o usuário!")
                
# Excluir usuário                  
async def delete_user(users_collection, address_collection, carts_collection, user_email):
    await address_models.delete_address(address_collection, user_email)
    await cart_models.delete_cart(carts_collection, user_email)
    
    user = await user_models.delete_user(users_collection, user_email)
    if user.deleted_count:
        return "Usuário deletado com sucesso!"
    raise HTTPException(status_code=404, detail ="Não há usuário com este email para ser deletado!")