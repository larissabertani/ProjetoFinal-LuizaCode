from typing import Optional
from pydantic import BaseModel, Field
from bson import ObjectId
from bson.objectid import ObjectId

from src.utils.pydantic_objectId import PyObjectId


class ProductSchema(BaseModel):
    id: PyObjectId | str = Field(default_factory=PyObjectId, alias="_id")
    name: str = Field(max_length=100)
    description: str
    price: float
    image: str
    code: int 
    type_animal: str
    category: str
    qt_stock: int

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        allow_population_by_field_name = True
        smart_union = True
        schema_extra = {
            "example": {
                    "name": "Ração 4",
                    "description": "Raças Específicas Lhasa Apso Cães Adultos",
                    "price": 99.99,
                    "image": "https://static.petz.com.br/fotos/1656091760542.jpg",
                    "code": 5643,
                    "type_animal": "dog",
                    "category": "food",
                    "qt_stock": 6
            }
        }
        
class ProductResponse(BaseModel):
    description: str
    result: Optional[ProductSchema] = None
    
class ProductUpdate(BaseModel):
    name: str = Field(max_length=100)
    description: str
    price: float
    image: str
    type_animal: str
    category: str
    qt_stock: int