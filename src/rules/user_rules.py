"""
Regras e ajustes para usuários (clientes)

"""

import src.models.user as user_models


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
    user_models.get_user(users_collection, user_id)
    
async def get_users(users_collection, skip, limit):
    user_models.get_users(users_collection, skip, limit)
         
async def get_user_by_email(users_collection, email):
    user = await user_models.get_user_by_email(users_collection, email)
    if user:
        return user
    return "Este e-mail não possuí cadastro!"
              
async def update_user(users_collection, user_id, user_data):
    user_models.update_user(users_collection, user_id, user_data)
                  
async def delete_user(users_collection, user_id):
    user_models.delete_user(users_collection, user_id)