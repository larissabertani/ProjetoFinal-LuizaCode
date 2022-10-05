from typing import List, Optional
from pydantic import BaseModel, Field
from bson import ObjectId
from bson.objectid import ObjectId

from src.schemas.user import UserSchema
from src.utils.pydantic_objectId import PyObjectId


class Address(BaseModel):
    street: str
    number: int
    zipcode: str
    district: str
    city: str
    state: str
    is_delivery: bool = Field(default=True)
    


class AddressSchema(BaseModel):
    # id: PyObjectId | str = Field(default_factory=PyObjectId, alias="_id")
    user: UserSchema
    addresses: List[Address] = []
    
class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        smart_union = True
        schema_extra = {
            "example": {
                  "user": {
                        "name": "iron Man",
                        "email": "ironMan@starkavengers.com",
                        "password": "hero123!",
                        "is_active": True,
                        "is_admin": False
                    },
                    "addresses" : [
                        {
                            "street": "i dont know",
                            "number": 13,
                            "zipcode": "9999-030",
                            "district": "Grass Lands",
                            "city": "stark tower",
                            "state": "Parallel Universe", 
                            "is_delivery": True
                        }, 
                        {
                            "street": "testing",
                            "number": 21,
                            "zipcode": "01020-040",
                            "district": "testing ",
                            "city": "example testing",
                            "state": "Parallel Universe", 
                            "is_delivery": False
                        }
                      ]
            }
        }

class AddressResponse(BaseModel):
    description: str
    result: Optional[AddressSchema] = None