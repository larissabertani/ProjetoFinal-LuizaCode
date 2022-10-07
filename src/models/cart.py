from csv import excel
from fastapi.encoders import jsonable_encoder

# Criar carrinho de compra
async def create_cart(carts_collection, cart):
    try:
        cart = jsonable_encoder(cart)
        return await carts_collection.insert_one(cart) 
    except Exception as e:
        print(f'create_cart.error: {e}')
        
# Consultar carrinho de compra        
async def get_cart(carts_collection, user_id):
    try:
        return await carts_collection.find_one({'user._id' : user_id})
    except Exception as e:
        print(f'get_cart.error: {e}')
        
# Atualizar carrinho    
async def update_cart(carts_collection, cart):
    try:
        return await carts_collection.update_one({'_id': cart['_id']}, {'$set': { 'cart_items': cart['cart_items'], 'total_price': cart['total_price']}})
    except Exception as e:
        print(f'update_cart.error: {e}')
        
# Remover produto do carrinho
async def delete_product_cart(carts_collection, cart, product_code: int):
    try:
        return await carts_collection.update_one({"_id": cart['_id']}, {"$pull": {"cart_items": { "product.code": product_code}}})
    except Exception as e:
        print(f'delete_product_cart.error: {e}')
    
# Remover produto de todos os carrinhos    
async def delete_product_all_cart(carts_collection, product_code: int):
    try:
        return await carts_collection.update_many({}, {"$pull": {"cart_items": { "product.code": product_code}}})
    except Exception as e:
        print(f'delete_product_all_cart.error: {e}')    
        
# Deletar carrinho
async def delete_cart(carts_collection, user_email):
    try:
    #    cart = jsonable_encoder(cart)
        return await carts_collection.delete_one({'user.email': user_email})
    except Exception as e:
        return f'delete_cart.error: {e}'
    
    
    
    
    

