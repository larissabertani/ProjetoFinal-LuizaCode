from typing import List, Optional
from pydantic import BaseModel
from bson.objectid import ObjectId

from src.schemas.product import ProductSchema
from src.schemas.user import UserSchema

class CartItemsSchema(BaseModel):
    product: ProductSchema
    qtd_product: int
    
class CartSchema(BaseModel):
    user: UserSchema
    cart_items: List[CartItemsSchema] = []
    total_price: float
    
    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        smart_union = True    
    
class CartResponse(BaseModel):
    description: str
    result: Optional[CartSchema] = None