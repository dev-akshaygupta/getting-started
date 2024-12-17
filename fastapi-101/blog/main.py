from fastapi import FastAPI, Depends, HTTPException, status, Response
from . import database, schemas, models
from sqlmodel import SQLModel, select
from sqlalchemy.orm import Session
from .hashing import Hash

app = FastAPI()

SQLModel.metadata.create_all(database.engine)

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()
    

@app.post("/addblog", status_code=status.HTTP_201_CREATED, tags=["Blogs"])
def create_blog(request: schemas.BlogCreate, db: Session = Depends(get_db)):
    new_blog = models.Blog(title=request.title, body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@app.delete("/blog/{id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Blogs"])
def delete_blog(id, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found!")
    blog.delete(synchronize_session=False)
    db.commit()
    return {'Blog is deleted successfully!'}

@app.put("/blog/{id}", status_code=status.HTTP_200_OK, tags=["Blogs"])
def update_blog(id, request: schemas.BlogCreate, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found!")
    blog.sqlmodel_update(request)
    db.commit()
    db.refresh(blog)
    return blog

@app.get("/allblogs", response_model=list[schemas.BlogRead], tags=["Blogs"])
def get_all_blogs(db: Session = Depends(get_db)):
    get_blogs = select(models.Blog)
    result = db.exec(get_blogs).all()
    return result

@app.get("/blog/{id}", response_model=schemas.BlogRead, tags=["Blogs"])
def get_blog(id:int, response: Response, db: Session = Depends(get_db)):
    get_blog = select(models.Blog).where(models.Blog.id == id)
    result = db.exec(get_blog).one_or_none()
    if not result:
        response.status_code = status.HTTP_404_NOT_FOUND
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found!")
    return result

@app.post("/createuser", status_code=status.HTTP_201_CREATED, tags=["Users"])
def create_user(request: schemas.UserCreate, db: Session = Depends(get_db)):
    new_user = models.User(name=request.name, email=request.email, password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user 

@app.get("/allusers", response_model=list[schemas.UserRead], tags=["Users"])
def get_all_users(db: Session = Depends(get_db)):
    get_user = select(models.User)
    result = db.exec(get_user).all()
    return result

@app.get("/user/{id}", response_model=schemas.UserRead, tags=["Users"])
def get_all_users(id:int, response: Response, db: Session = Depends(get_db)):
    get_user = select(models.User).where(models.User.id == id)
    result = db.exec(get_user).one_or_none()
    if not result:
        response.status_code = status.HTTP_404_NOT_FOUND
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found!")
    return result