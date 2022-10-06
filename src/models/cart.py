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
async def update_cart(cart_collection, cart):
    try:
        return await cart_collection.update_one({'_id': cart['_id']}, {'$set': { 'cart_items': cart['cart_items'], 'total_price': cart['total_price']}})
    except Exception as e:
        print(f'update_cart.error: {e}')
    
    
    
    
    
    
    

