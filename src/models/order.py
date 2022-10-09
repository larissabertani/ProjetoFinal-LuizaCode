import logs

# Criar pedido
async def create_order(order_collection, order):
    try:
        logs.info("Pedido criado")
        return await order_collection.insert_one(order)
    except Exception as e:
        logs.error("Erro ao criar carrinho")
        return f'create_order.error: {e}'

# Consultar quantos carrinhos fechados um cliente possui
async def get_order_by_email(order_collection, user_email, skip: int, limit: int):
    try:
        logs.info("Consulta realizada")
        orders_cursor = order_collection.find({'user.email' : user_email}).skip(int(skip)).limit(int(limit))          
        return await orders_cursor.to_list(length=int(limit))    
    except Exception as e:
        logs.error("Erro ao fazer consulta")
        return f'get_order_by_email.error: {e}'
        
# Consultar os produtos e suas quantidades em carrinhos fechados
async def get_order_by_id(order_collection, order_id):
    try:
        logs.info("Consulta realizada")
        return await order_collection.find_one({'_id' : order_id})          
    except Exception as e:
        logs.error("Erro ao fazer consulta")
        return f'get_order_items_by_id.error: {e}'      

# Excluir pedido
async def delete_order(order_collection, order_id):
    try:
        logs.info("Exclusão realizada")
        return await order_collection.delete_one({'_id': order_id})
    except Exception as e:
        logs.error("Erro ao fazer exclusão")
        return f'delete_order.error: {e}'