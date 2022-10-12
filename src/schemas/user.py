from typing import Optional
from bson import List
from pydantic import BaseModel, Field, SecretStr
from pydantic.networks import EmailStr
from bson.objectid import ObjectId

from src.utils.pydantic_objectId import PyObjectId

class UserSchema(BaseModel):
    id: PyObjectId | str = Field(default_factory=PyObjectId, alias="_id")
    name: str
    email: EmailStr = Field(unique=True, index=True)
    password: SecretStr = Field(...)
    is_active: bool = Field(default=True)
    is_admin: bool = Field(default=False)
    
    def __str__(self) -> str:
        return str(self.id)

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        smart_union = True
        schema_extra = {
            "example": {
                "name": "Testando Silva",
                "email": "testando@gmail.com",
                "password": "*****"
            }
        }
        
class UserUpdate(BaseModel):
    name: Optional[str]
    email: Optional[EmailStr]
    password: Optional[str]
    
class UserResponse(BaseModel):
    description: str
    result: UserSchema | List[UserSchema] = None