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
                "name": "Book Alice in the wonderland",
                "description": "It details the story of a young girl named Alice who falls through a rabbit hole into a fantasy world of anthropomorphic creatures",
                "price": 569.9,
                "image": "http://127.0.0.1:8000/produto/aliceinthewordeland.png",
                "code": 987654321,
                "type_animal": "dog",
                "category": "food",
                "qt_stock": 15
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