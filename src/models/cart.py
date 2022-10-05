from src.schemas.user import UserSchema
from src.models.user import get_user
from src.schemas.cart import CartTotalSchema

# Passar dados do produto e usuário
async def create_cart(cart: CartTotalSchema):
    # Verificar se carrinho para este usuário está aberto
    # cart_data = { # adicionar produto e quantidade flag no carrinho se aberto true  e verificar se há carrinho no banco aberto/fechado de acordo com usuário
    #             "user": user,
    #             "product_id": product_id,
    #             "quantity": quantity,
    #             "price": price,
    #             "address": address, # endereço no order
    #             "paid": False,
    #             "create": datetime.now(),
    #             "authority": ""
                
    #         }
    print(cart)