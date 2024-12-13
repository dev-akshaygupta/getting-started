from sqlmodel import SQLModel

# Blog Schema
class BlogCreate(SQLModel):
    title: str
    body: str