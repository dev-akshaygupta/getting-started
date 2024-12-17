from pydantic import BaseModel, ConfigDict
from typing import List

# Blog Schemas
class BlogCreate(BaseModel):
    title: str
    body: str
    
class BlogRead(BaseModel):
    title: str
    body: str
    creator: "UserRead"
    class Config():
        model_config = ConfigDict(from_attributes=True)

# User Schemas
class UserCreate(BaseModel):
    name: str
    email: str
    password: str
    
class UserRead(BaseModel):
    name: str
    email: str
    blogs: List["BlogCreate"]
    class Config():
        model_config = ConfigDict(from_attributes=True)
        
# Login Schema
class Login(BaseModel):
    username: str
    password: str

# JWT Token Schema
class Token(BaseModel):
    access_token: str
    token_type: str
 
class TokenData(BaseModel):
    email: str | None = None