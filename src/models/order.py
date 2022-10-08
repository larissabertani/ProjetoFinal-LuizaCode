
# Criar pedido
import asyncio


async def create_order(order_collection, order):
    try:
        return await order_collection.insert_one(order)
    except Exception as e:
        print(f'create_order.error: {e}')


# Consultar os carrinhos fechados de um cliente
def get_order_by_email3(order_collection, user_email):
    orders_list = []
    try:
        orders = order_collection.find({'user.email': {"$in": user_email}})
        for order in orders:
            orders_list.append(order)
    except Exception as e:
        print(f'get_order_by_email.error: {e}')
    print(orders_list)
    return orders_list

# Consultar os produtos e suas quantidades em carrinhos fechados
async def get_product(order_collection, product_code):
    try:
        return await order_collection.aggregate([    
            { "$match": { "order_items": { "product.code": product_code } } },
            { "$group": { "product.code": 1, "count": { "qtd_product": 1 } }}
        ])    
    
    except Exception as e:
        print(f'get_product.error: {e}')

# Deletar order
async def delete_order(order_collection, order_id):
    try:
        return await order_collection.delete_one({'_id': order_id})
    except Exception as e:
        return f'delete_order.error: {e}'