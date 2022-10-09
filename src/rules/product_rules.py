"""
Regras e ajustes para produtos

"""

import src.models.product as product_models
from src.rules.cart_rules import delete_product_all_cart

# Criar produto
async def create_product(products_collection, product):
    if product['price'] <= 0.01:
        return "O valor do produto deve ser superior a R$0,01"
    if product['qt_stock'] <= 0:
        return "A quantidade do produto deve ser superior a 0"
    has_product = await product_models.get_product_by_code(products_collection, product['code'])
    if has_product:
        return "Já existe produto cadastrado com este código!"    
    new_product = await product_models.create_product(products_collection, product)
    if new_product.inserted_id:
        return await product_models.get_product_by_id(products_collection, new_product.inserted_id)
    return "O produto não atende os requisitos de criação, não foi possível criá-lo."

# Obter produto pelo id
async def get_product_by_id(products_collection, product_id):
    product = await product_models.get_product_by_id(products_collection, product_id)
    if product:
        return product
    return "Não existe produto com este id!"

# Obter produto pelo código
async def get_product_by_code(products_collection, product_code):
    product = await product_models.get_product_by_code(products_collection, product_code)
    if product:
        return product
    return "Não existe produto com este código!"

# Obter produto pelo nome
async def get_product_by_name(products_collection, product_name):
    product = await product_models.get_product_by_name(products_collection, product_name)
    if product:
        return product
    return "Não existe produto com este nome!"

async def update_product(products_collection, product_code, product):
    product_storaged = await product_models.get_product_by_code(products_collection, product_code)
    if product_storaged:
        product_updated = await product_models.update_product(products_collection, product_code, product.dict())
        if product_updated.modified_count:
            return "Produto alterado com sucesso!"
        return "Erro ao atualizar o produto!"
    return "Não existe produto com o código informado!"

# Excluir produto
async def delete_product(product_collection, carts_collection, product_code: int):    
    await delete_product_all_cart(carts_collection, product_code)    
    product = await product_models.delete_product(product_collection, product_code)
    if product.deleted_count:
        return "Produto deletado com sucesso!"
    return "Não há produto com este código para ser deletado!"
