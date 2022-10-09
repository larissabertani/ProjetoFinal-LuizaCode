
from src.schemas.order import OrderResponse
import src.rules.order_rules as order_rules
from bson.objectid import ObjectId
from fastapi import APIRouter, Request


router = APIRouter()

# Consultar os carrinhos fechados de um cliente
@router.get("/{user_email}/skip/{skip}/limit/{limit}", response_description="get orders", response_model=OrderResponse)
async def route_get_order(request: Request, user_email, skip, limit):
    response = await order_rules.get_order_by_email(request.app.database.order_collection, user_email, skip, limit)
    return await process_order_response(response)

# Consultar quantos carrinhos fechados um cliente possui
@router.get("/count/{user_email}", response_description="get order count", response_model=OrderResponse)
async def route_get_order(request: Request, user_email):
    response = await order_rules.get_order_by_email(request.app.database.order_collection, user_email, 0, 1000)    
    if type(response) == str:
        return await process_order_response(response)
    return await process_order_response(len(response))

# Consultar os produtos e suas quantidades em carrinhos fechados
@router.get("/items/{order_id}", response_description="get product qty", response_model=OrderResponse)
async def route_get_items_by_id(request: Request, order_id: str):
    response = await order_rules.get_order_items_by_id(request.app.database.order_collection, order_id)
    return await process_order_response(response)

# Excluir pedido do cliente
@router.delete("/{order_id}")
async def route_delete_order(order_id: str, request: Request):
    response = await order_rules.delete_order(request.app.database.order_collection, ObjectId(order_id))
    return await process_order_response(response)

# process result
async def process_order_response(response):
    if type(response) == str:
        return OrderResponse(description = response)
    return OrderResponse(description = 'OK', result = response)