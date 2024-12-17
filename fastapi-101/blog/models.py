from sqlmodel import SQLModel, Field, Relationship
from typing import List, Optional


# Blog Table
class Blog(SQLModel, table=True):
    __tablename__ = "blogs"
    
    id: int = Field(primary_key=True, index=True)
    title: str
    body: str
    creator_id: Optional[int] = Field(default=None, foreign_key="users.id")
    
    creator: "User" = Relationship(back_populates="blogs")

# User Table
class User(SQLModel, table=True):
    __tablename__ = "users"
    
    id: int = Field(primary_key=True, index=True)
    name: str
    email: str
    password: str
    
    blogs: List["Blog"] = Relationship(back_populates="creator")