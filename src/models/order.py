
# Criar pedido
async def create_order(order_collection, order):
    try:
        return await order_collection.insert_one(order)
    except Exception as e:
        print(f'create_order.error: {e}')


# Consultar os carrinhos fechados de um cliente
async def get_order_by_email(order_collection, user_email):
    try:
        return await order_collection.find_one({'user.email': user_email})
    except Exception as e:
        print(f'get_order_by_email.error: {e}')

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