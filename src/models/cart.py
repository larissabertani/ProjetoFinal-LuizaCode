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
        

# Deletar carrinho
async def delete_cart(carts_collection, user_email):
    try:
    #    cart = jsonable_encoder(cart)
        return await carts_collection.delete_one({'user.email': user_email})
    except Exception as e:
        return f'delete_cart.error: {e}'
    
    
    
    
    
    
    

