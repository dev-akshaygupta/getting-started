from fastapi import FastAPI
from .database import engine
from sqlmodel import SQLModel
from .routers import blog, user, authentication

app = FastAPI()

SQLModel.metadata.create_all(engine)

app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)