import logs

# Criar usuário 
async def create_user(users_collection, user):
    try:
        logs.info("Usuário criado")
        return await users_collection.insert_one(user)
    except Exception as e:
        logs.error("Erro ao criar usuário")
        return f'create_user.error: {e}'
 
# Obter usuário pelo id
async def get_user(users_collection, user_id):
    try:
        logs.info("Consulta realizada")
        return await users_collection.find_one({"_id": user_id})
    except Exception as e:
        logs.error("Erro ao fazer consulta")
        return f'get_user.error: {e}'
 
# Obter lista de usuários
async def get_users(users_collection, skip, limit):
    try:
        logs.info("Consulta realizada")
        user_cursor = users_collection.find().skip(int(skip)).limit(int(limit))
        users = await user_cursor.to_list(length=int(limit))
        return users
    except Exception as e:
        logs.error("Erro ao fazer consulta")
        return f'get_users.error: {e}'

# Obter usuário pelo e-mail
async def get_user_by_email(users_collection, email):
    try:
        logs.info("Consulta realizada")
        user = await users_collection.find_one({'email': email})
        return user
    except Exception as e:
        logs.error("Erro ao fazer consulta")
        return f'get_user_by_email.error: {e}'

# Atualizar usuário
async def update_user(users_collection, user_id, user_data):
    try:
        logs.info("Usuário atualizado")
        data = {k: v for k, v in user_data.items() if v is not None}

        user = await users_collection.update_one(
            {'_id': user_id},
            {'$set': data}
        )

        if user.modified_count:
            return True, user.modified_count

        return False, 0
    except Exception as e:
        logs.error("Erro ao atualizar usuário")
        return f'update_user.error: {e}'

# Excluir usuário
async def delete_user(users_collection, user_email):
    try:
        logs.info("Usuário excluído")
        return await users_collection.delete_one({'email': user_email})
    except Exception as e:
        logs.error("Erro ao excluir usuário")
        return f'delete_user.error: {e}'
