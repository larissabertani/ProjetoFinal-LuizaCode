# Criar produto
async def create_product(products_collection, product):
    try:
        return await products_collection.insert_one(product)
    except Exception as e:
        return f'create_product.error: {e}'

# Obter produto pelo id
async def get_product_by_id(products_collection, product_id):
    try:
        return await products_collection.find_one({'_id': product_id})
    except Exception as e:
        return f'get_product_by_id.error: {e}'

# Obter produto pelo códgo
async def get_product_by_code(products_collection, product_code: int):
    try:
        return await products_collection.find_one({'code': product_code})
    except Exception as e:
        return f'get_product_by_code.error: {e}'

# Obter produto pelo nome
async def get_product_by_name(products_collection, product_name):
    try:
        return await products_collection.find_one({'name': product_name})
    except Exception as e:
        return f'get_product_by_name.error: {e}'
    
# Obter lista de produtos
async def get_products(products_collection, skip, limit):
    try:
        product_cursor = products_collection.find().skip(int(skip)).limit(int(limit))
        products = await product_cursor.to_list(length=int(limit))
        return products
    except Exception as e:
        return f'get_products.error: {e}'

# Atualizar produto (exceto código)
async def update_product(products_collection, product_code, product):
    try:
        return await products_collection.update_one({'code': product_code}, {'$set': product})
    except Exception as e:
        return f'update_product.error: {e}'

# Excluir produto
async def delete_product(products_collection, product_code):
    try:
        return await products_collection.delete_one({'code': product_code})
    except Exception as e:
        return f'delete_product.error: {e}'
