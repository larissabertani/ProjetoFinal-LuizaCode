async def create_product(products_collection, product):
    try:
        return await products_collection.insert_one(product)
    except Exception as e:
        print(f'create_product.error: {e}')

async def get_product_by_id(products_collection, product_id):
    try:
        return await products_collection.find_one({'_id': product_id})
    except Exception as e:
        print(f'get_product_by_id.error: {e}')
        
async def get_product_by_code(products_collection, product_code):
    try:
        return await products_collection.find_one({'code': product_code})
    except Exception as e:
        print(f'get_product_by_code.error: {e}')
        
async def get_product_by_name(products_collection, product_name):
    try:
        return await products_collection.find_one({'name': product_name})
    except Exception as e:
        print(f'get_product_by_name.error: {e}')

async def get_products(products_collection, skip, limit):
    try:
        product_cursor = products_collection.find().skip(int(skip)).limit(int(limit))
        products = await product_cursor.to_list(length=int(limit))
        return products

    except Exception as e:
        print(f'get_products.error: {e}')

async def update_product(products_collection, product_code, product_data):
    try:
        data = {k: v for k, v in product_data.items() if v is not None}

        product = await products_collection.update_one(
            {'code': product_code},
            {'$set': data}
        )

        if product.modified_count:
            return True, product.modified_count

        return False, 0
    except Exception as e:
        print(f'update_product.error: {e}')

async def delete_product(products_collection, product_code):
    try:
        return await products_collection.delete_one({'code': product_code})
    except Exception as e:
        print(f'delete_product.error: {e}')
