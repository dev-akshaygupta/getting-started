from pydantic import BaseModel

# Blog Schema
class BlogCreate(BaseModel):
    title: str
    body: str
    
class BlogRead(BaseModel):
    id: int
    title: str
    body: str
