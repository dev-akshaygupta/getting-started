from pydantic import BaseModel, ConfigDict

# Blog Schema
class BlogCreate(BaseModel):
    title: str
    body: str
    
class BlogRead(BaseModel):
    title: str
    body: str
    class Config():
        model_config = ConfigDict(from_attributes=True)

class UserCreate(BaseModel):
    name: str
    email: str
    password: str
    
class UserRead(BaseModel):
    name: str
    email: str
    class Config():
        model_config = ConfigDict(from_attributes=True)