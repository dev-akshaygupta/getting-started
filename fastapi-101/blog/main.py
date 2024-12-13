from fastapi import FastAPI
from . import models, database
from sqlmodel import SQLModel

app = FastAPI()

SQLModel.metadata.create_all(database.engine)

@app.post("/blog")
def create(request: models.Blog):
    return {'title':request.title, 'body':request.body} 