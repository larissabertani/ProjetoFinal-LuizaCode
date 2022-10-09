"""
Regras e ajustes para endereços de clientes

"""
import src.models.address as address_models
import src.models.user as user_models
from fastapi import HTTPException

# Criar endereço do usuário
async def create_user_address(address_collection, users_collection, user_email, new_address):# = []):
    user = await user_models.get_user_by_email(users_collection, user_email)
    if (not user):
        return "Não há usuário cadastrado com este email!"
    
    user_address = await address_models.get_address_by_user(address_collection, user_email)     
    
    if (not user_address):
        new_user_address = await address_models.create_user_address(address_collection, {
            "user": user,
            "addresses": new_address
        })
        if new_user_address.inserted_id:
            new_user_address = await address_models.get_address_by_id(address_collection, new_user_address.inserted_id)
    
    else:
        for new_ad in new_address:
            if new_ad not in user_address["addresses"]:
                user_address["addresses"].append(new_ad)
                
        await address_models.update_address(address_collection, user_address["_id"], user_address["addresses"])        
        new_user_address = await address_models.get_address_by_id(address_collection, user_address["_id"])
    return new_user_address

# Obter endereço do usuário
async def get_address_by_user(address_collection, user_email):
    user_address = await address_models.get_address_by_user(address_collection, user_email)
    if user_address:
        return user_address
    raise HTTPException(status_code=404, detail="Não há usuário cadastrado com este email!")
    # return "Não há usuário cadastrado com este email!"

# Excluir endereço do usuário
async def delete_address(address_collection, user_email):
    address = await address_models.delete_address(address_collection, user_email)
    if address.deleted_count:
        return "Endereço deletado com sucesso!"
    raise HTTPException(status_code=404, detail="Não há endereço para ser deletado para este usuário!")
    #return "Não há endereço para ser deletado para este usuário!"
    