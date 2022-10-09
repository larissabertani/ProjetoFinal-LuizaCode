
async def create_user_address(address_collection, user_address):
    try:
        return await address_collection.insert_one(user_address) 
    except Exception as e:
        print(f'create_address.error: {e}')

async def update_address(address_collection, id_user_address, addresses):
    try:
        return await address_collection.update_one({'_id': id_user_address}, {'$set': { "addresses": addresses}})
    except Exception as e:
        print(f'update_addresses.error: {e}')
        
async def get_address_by_user(address_collection, user_email):
    try:
        return await address_collection.find_one({'user.email': user_email})
    except Exception as e:
        print(f'get_address_by_user.error: {e}')
        
async def get_address_by_id(address_collection, user_address_id):
    try:
        return await address_collection.find_one({'_id': user_address_id})
    except Exception as e:
        print(f'get_address_by_id.error: {e}')
        
# async def get_address_delivery_by_email(address_collection, user_email):
#     try:
#         return await address_collection.find_one({"$and": [{'user.email': user_email, 'addresses.is_delivery' : True}]})
#         #({}, {"$pull": {"cart_items": { "product.code": product_code}}})
#         #find_one({'user.email' : user_email})
#     except Exception as e:
#         print(f'get_address_by_user.error: {e}')
        
async def get_delivery_address(address_collection, user_email):
    user_addresses = await get_address_by_user(address_collection, user_email)
    
    if user_addresses:
        for address in user_addresses["addresses"]:
            if address["is_delivery"]:
                return address
    return "Erro ao obter endereço de entrega"  

async def delete_address(address_collection, user_email):
    try:
        return await address_collection.delete_one({'user.email': user_email})
    except Exception as e:
        return f'delete_address.error: {e}'
    
    
    