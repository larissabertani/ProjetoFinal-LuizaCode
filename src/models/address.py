import logs

# Criar endereço do usuário
async def create_user_address(address_collection, user_address):
    try:
        logs.info("Endereço criado para o usuário")
        return await address_collection.insert_one(user_address) 
    except Exception as e:
        logs.error("Erro ao criar endereço do usuário")
        return f'create_address.error: {e}'


# Atualizar endereço do usuário
async def update_address(address_collection, id_user_address, addresses):
    try:
        logs.info("Endereço atualizado para o usuário")
        return await address_collection.update_one({'_id': id_user_address}, {'$set': { "addresses": addresses}})
    except Exception as e:
        logs.error("Erro ao atualizar endereço do usuário")
        return f'update_addresses.error: {e}'
    
    
# Consultar endereço do usuário pelo e-mail       
async def get_address_by_user(address_collection, user_email):
    try:
        logs.info("Consulta do usuário realizada")
        return await address_collection.find_one({'user.email': user_email})
    except Exception as e:
        logs.error("Erro ao consultar o usuário")
        return f'get_address_by_user.error: {e}'


# Consultar endereço do usuário pelo id        
async def get_address_by_id(address_collection, user_address_id):
    try:
        logs.info("Consulta do usuário realizada")
        return await address_collection.find_one({'_id': user_address_id})
    except Exception as e:
        logs.error("Erro ao consultar o usuário")
        return f'get_address_by_id.error: {e}'
        

# Consultar endereço de entrega do usuário
async def get_delivery_address(address_collection, user_email):
    user_addresses = await get_address_by_user(address_collection, user_email)
    
    if user_addresses:
        for address in user_addresses["addresses"]:
            if address["is_delivery"]:
                return address
    return "Erro ao obter endereço de entrega"  


# Excluir endereço do usuário
async def delete_address(address_collection, user_email):
    try:
        logs.info("Usuário excluído")
        return await address_collection.delete_one({'user.email': user_email})
    except Exception as e:
        logs.error("Erro ao excluir o usuário")
        return f'delete_address.error: {e}'
    
    
    