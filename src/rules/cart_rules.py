"""
Regras e ajustes para carrinhos

"""

from fastapi import HTTPException
from src.models.user import get_user
from src.models.product import get_product_by_code
from src.schemas.cart import CartItemsSchema, CartSchema
from src.schemas.product import ProductSchema
import src.models.cart as cart_models
from fastapi.encoders import jsonable_encoder


async def create_cart(carts_collection, users_collection, user_id):
    cart = await cart_models.get_cart(carts_collection, user_id)
    if not cart:
        user = await get_user(users_collection, user_id)
        if user:
            cart = CartSchema(user = user, cart_items = [], total_price = 0)
            new_cart = await cart_models.create_cart(carts_collection, cart)
            if new_cart.inserted_id:
                return await cart_models.get_cart(carts_collection, user_id)        
            return "Ocorreu um erro ao criar o carrinho!"
        return "Não há usuário cadastrado com este id." 
    return cart        
            
# Adicionar produto ao carrinho
async def add_item_cart(carts_collection, users_collection, products_collection, user_id, product_code):
    product = await get_product_by_code(products_collection, product_code)
    if product:
        cart = await cart_models.get_cart(carts_collection, user_id)
        if not cart:
            cart = await create_cart(carts_collection, users_collection, user_id)
        if type(cart) == str:
            return cart
        has_item = False
        for item in cart['cart_items']:
            if item['product']['code'] == product_code:
                item['qtd_product'] += 1
                has_item = True
                break
        if not has_item: 
            cart_item = jsonable_encoder(CartItemsSchema(product = product, qtd_product = 1))
            cart['cart_items'].append(cart_item)
        await calculate_cart_price(cart)
        cart = await cart_models.update_cart(carts_collection, cart)
        if cart.modified_count:
            return await cart_models.get_cart(carts_collection, user_id)
        return "Erro ao atualizar o carrinho!"
    return "Não existe produto com este código!"
           
    
# Calcular preço total do carrinho    
async def calculate_cart_price(cart):
    price: float = 0
    for item in cart['cart_items']:
        price += item['product']['price'] * item['qtd_product']
    cart['total_price'] = price #sum(item['product']['price'] for item in cart['cart_items'])
    
    
# Consultar carrinho pelo id do usuário
async def get_cart(carts_collection, user_id):
    cart = await cart_models.get_cart(carts_collection, user_id)
    if cart:
        return cart
    return "Este id não possui carrinho aberto!"


async def delete_cart(carts_collection, user_email):
    cart = await cart_models.delete_cart(carts_collection, user_email)
    if cart.deleted_count:
        return "Carrinho deletado com sucesso!"
    # raise HTTPException(status_code=404, detail="Não há carrinho para ser deletado para este usuário!")
    return "Não há carrinho para ser deletado para este usuário!"
    