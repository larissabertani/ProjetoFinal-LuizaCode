from urllib import response
from fastapi.encoders import jsonable_encoder
from fastapi import APIRouter, Request, Body, status

import src.rules.product_rules as product_rules
from src.schemas.product import ProductResponse, ProductSchema, ProductResponse, ProductUpdate


router = APIRouter()


# create product
@router.post("/", response_description="Create a new product", response_model=ProductResponse)
async def route_post_product(requests: Request, new_product: ProductSchema = Body(...)):
    new_product = jsonable_encoder(new_product)
    response = await product_rules.create_product(requests.app.database.product_collection, new_product)
    return await process_product_response(response)
    

# get product by name
@router.get("/name/{name}", response_description="Get a product by name", response_model=ProductResponse)
async def route_get_product_by_name(request: Request, name: str):
    response = await product_rules.get_product_by_name(request.app.database.product_collection, name)
    return await process_product_response(response)

# get product by code
@router.get("/code/{code}", response_description="Get a product by code", response_model=ProductResponse)
async def route_get_product_by_code(code: int, request: Request):
    response = await product_rules.get_product_by_code(request.app.database.product_collection, code)
    return await process_product_response(response)

# update product by code
@router.put("/{code}", response_description="Update a product by code", response_model=ProductResponse)
async def route_update_product_by_code(code: int, request: Request, product: ProductUpdate = Body(...)):
    response = await product_rules.update_product(request.app.database.product_collection, code, product)
    return await process_product_response(response)

# delete product by code
@router.delete("/{code}", response_description="Delete a product")
async def route_delete_product(code: int, request: Request):
    response = await product_rules.delete_product(request.app.database.product_collection, code)
    return await process_product_response(response)

# process result
async def process_product_response(response):
    if type(response) == str:
        return ProductResponse(description = response)
    return ProductResponse(description = 'OK', result = response)