from sqlmodel import SQLModel

# Blog Schema
class BlogCreate(SQLModel):
    title: str
    body: str
    
class BlogRead(SQLModel):
    id: int
    title: str
    body: str
    
    class Config:
        orm_mode = True
