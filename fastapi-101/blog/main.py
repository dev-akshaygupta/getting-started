from fastapi import FastAPI
from .database import engine
from sqlmodel import SQLModel
from .routers import blog, user, authentication

# Entry point of the FastAPI App
app = FastAPI()

# Create all the database tables defined with SQLModels
SQLModel.metadata.create_all(engine)

# All the routes
app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)