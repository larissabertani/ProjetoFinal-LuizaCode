import logs
from fastapi.encoders import jsonable_encoder

# Criar carrinho de compra
async def create_cart(carts_collection, cart):
    try:
        logs.info("Carrinho criado")
        cart = jsonable_encoder(cart)
        return await carts_collection.insert_one(cart) 
    except Exception as e:
        logs.error("Erro ao criar carrinho")
        return f'create_cart.error: {e}'
        
        
# Consultar carrinho de compra do usuário pelo id       
async def get_cart(carts_collection, user_id):
    try:
        logs.info("Consulta de carrinho realizada")
        return await carts_collection.find_one({'user._id' : user_id})
    except Exception as e:
        logs.error("Erro ao consultar carrinho")
        return f'get_cart.error: {e}'
        
        
# Consultar carrinho de compra pelo e-mail       
async def get_cart_by_email(carts_collection, user_email):
    try:
        logs.info("Consulta de carrinho realizada")
        return await carts_collection.find_one({'user.email' : user_email})
    except Exception as e:
        logs.error("Erro ao consultar carrinho")
        return f'get_cart_by_email.error: {e}'
        
        
# Atualizar carrinho    
async def update_cart(carts_collection, cart):
    try:
        logs.info("Atualização de carrinho realizada")
        return await carts_collection.update_one({'_id': cart['_id']}, {'$set': { 'cart_items': cart['cart_items'], 'total_price': cart['total_price']}})
    except Exception as e:
        logs.error("Erro ao atualizar carrinho")
        return f'update_cart.error: {e}'
        
# Remover produto do carrinho
async def delete_product_cart(carts_collection, cart, product_code: int):
    try:
        logs.info("Remoção de produto do carrinho realizada")
        return await carts_collection.update_one({"_id": cart['_id']}, {"$pull": {"cart_items": { "product.code": product_code}}})
    except Exception as e:
        logs.error("Erro ao remover produto do carrinho")
        return f'delete_product_cart.error: {e}'
    
# Remover produto de todos os carrinhos    
async def delete_product_all_cart(carts_collection, product_code: int):
    try:
        logs.info("Remoção de produtos do carrinho realizada")
        return await carts_collection.update_many({}, {"$pull": {"cart_items": { "product.code": product_code}}})
    except Exception as e:
        logs.error("Erro ao remover produtos do carrinho")
        return f'delete_product_all_cart.error: {e}'    
        
# Exluir carrinho do usuário
async def delete_cart(carts_collection, user_email):
    try:
        logs.info("Exclusão do carrinho realizada")
        return await carts_collection.delete_one({'user.email': user_email})
    except Exception as e:
        logs.error("Erro excluir carrinho")
        return f'delete_cart.error: {e}'
    
# Excluir carrinho vazio
async def delete_empty_cart(carts_collection):
    try:
        logs.info("Exclusão do carrinho realizada")
        return await carts_collection.delete_many({'cart_items': { '$size': 0 }})
    except Exception as e:
        logs.error("Erro excluir carrinho")
        return f'delete_empty_cart.erro {e}'
    
