
# Criar pedido
import asyncio
from fastapi.responses import JSONResponse



async def create_order(order_collection, order):
    try:
        return await order_collection.insert_one(order)
    except Exception as e:
        print(f'create_order.error: {e}')


# Consultar quantos carrinhos fechados um cliente possui
async def get_order_by_email(order_collection, user_email, limit: int):
    try:
        orders_cursor = order_collection.find({'user.email' : user_email}).skip(int(0)).limit(int(limit))          
        return await orders_cursor.to_list(length=int(limit))    
            
    except Exception as e:
        print(f'get_order_by_email.error: {e}')

# Consultar os produtos e suas quantidades em carrinhos fechados
async def get_order(order_collection, order_id):
    try:
        return await order_collection.find_one({'order._id' : order_id})
    except Exception as e:
        print(f'get_order.error: {e}')

# Deletar order
async def delete_order(order_collection, order_id):
    try:
        return await order_collection.delete_one({'_id': order_id})
    except Exception as e:
        return f'delete_order.error: {e}'