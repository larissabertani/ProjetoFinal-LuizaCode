from typing import List, Optional
from pydantic import BaseModel
from src.schemas.user import UserSchema

class CartSchema(BaseModel):
    user: UserSchema
    product_id: str
    price: float
    quantity: int

    
class CartTotalSchema(BaseModel):
    itens: List[CartSchema]
    total_price: float
    open: bool
    
    
class CartResponse(BaseModel):
    itens: List[CartSchema]
    open: bool