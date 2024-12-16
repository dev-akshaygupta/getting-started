from pydantic import BaseModel

# Blog Schema
class BlogCreate(BaseModel):
    title: str
    body: str
    
class BlogRead(BaseModel):
    title: str
    body: str
    class Config():
        orm_mode = True
