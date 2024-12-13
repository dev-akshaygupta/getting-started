from fastapi import FastAPI, Depends, HTTPException, status, Response
from . import database, schemas, models
from sqlmodel import SQLModel, select
from sqlalchemy.orm import Session

app = FastAPI()

SQLModel.metadata.create_all(database.engine)

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()
    

@app.post("/addblog", status_code=status.HTTP_201_CREATED)
def create_blog(request: schemas.BlogCreate, db: Session = Depends(get_db)):
    new_blog = models.Blog(title=request.title, body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@app.get("/allblogs", response_model=list[schemas.BlogRead])
def get_all_blogs(db: Session = Depends(get_db)):
    get_blogs = select(models.Blog)
    result = db.exec(get_blogs).all()
    return result

@app.get("/blog/{id}", response_model=schemas.BlogRead)
def get_blog(id:int, response: Response, db: Session = Depends(get_db)):
    get_blog = select(models.Blog).where(models.Blog.id == id)
    result = db.exec(get_blog).one_or_none()
    if not result:
        response.status_code = status.HTTP_404_NOT_FOUND
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found!")
    return result
