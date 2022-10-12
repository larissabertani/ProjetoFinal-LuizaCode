import datetime
from decimal import Decimal
from typing import List, Optional
from pydantic import BaseModel, Field
from bson.objectid import ObjectId
from src.utils.pydantic_objectId import PyObjectId

from src.schemas.address import Address
from src.schemas.user import UserSchema
from src.schemas.cart import CartItemsSchema

class OrderSchema(BaseModel):
    id: PyObjectId | str = Field(default_factory=PyObjectId, alias="_id")
    user: UserSchema
    price: Decimal #= Field(max_digits=100, decimal_places=2)
    paid: bool = Field(default=True)
    create: datetime.datetime = Field(default=datetime.datetime.now())
    address: Address
    authority: Optional[str] = Field(max_length=100)
    order_items: List[CartItemsSchema] = []
    
    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True  # required for the _id
        json_encoders = {ObjectId: str}
        smart_union = True

class OrderResponse(BaseModel):
    description: str
    result: Optional[OrderSchema] | Optional[List[OrderSchema]] | Optional[List[CartItemsSchema]] | int = None