
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
        
async def get_one_address(address_collection, user_id):
    find_address = await get_address_by_user(address_collection, user_id)
    
    if find_address:
        for add in find_address["addresses"]:
            if add["is_delivery"]:
                return add
    return "FALHA"  

async def delete_address(address_collection, user_email):
    try:
        return await address_collection.delete_one({'user.email': user_email})
    except Exception as e:
        return f'delete_address.error: {e}'
    
    
    