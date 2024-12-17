from fastapi import APIRouter, Depends, HTTPException, status, Response
from .. import schemas, models, database
from sqlalchemy.orm import Session
from sqlmodel import select
from typing import List

router = APIRouter(
    prefix="/v1/blog",
    tags=["Blogs"]
)

# Create Blog
@router.post("/create", status_code=status.HTTP_201_CREATED)
def create_blog(request: schemas.BlogCreate, db: Session = Depends(database.get_db)):
    new_blog = models.Blog(title=request.title, body=request.body, creator_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

# Delete Blog
@router.delete("/delete/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(id, db: Session = Depends(database.get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found!")
    blog.delete(synchronize_session=False)
    db.commit()
    return {'Blog is deleted successfully!'}

# Update Blog
@router.put("/update/{id}", status_code=status.HTTP_200_OK)
def update_blog(id, request: schemas.BlogCreate, db: Session = Depends(database.get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found!")
    blog.sqlmodel_update(request)
    db.commit()
    db.refresh(blog)
    return blog

# Get All Blogs
@router.get("/all", response_model=List[schemas.BlogRead])
def get_all_blogs(db: Session = Depends(database.get_db)):
    get_blogs = select(models.Blog)
    result = db.exec(get_blogs).all()
    return result

# Get Blog by ID
@router.get("/{id}", response_model=schemas.BlogRead)
def get_blog(id:int, response: Response, db: Session = Depends(database.get_db)):
    get_blog = select(models.Blog).where(models.Blog.id == id)
    result = db.exec(get_blog).one_or_none()
    if not result:
        response.status_code = status.HTTP_404_NOT_FOUND
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found!")
    return result