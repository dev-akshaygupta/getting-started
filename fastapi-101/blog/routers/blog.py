from fastapi import APIRouter, Depends, status, Response
from .. import schemas, database, oAuth2
from sqlalchemy.orm import Session
from sqlmodel import select
from typing import List
from ..repository import blog

router = APIRouter(
    prefix="/v1/blog",
    tags=["Blogs"]
)

# Create Blog
@router.post("/create", status_code=status.HTTP_201_CREATED)
def create_blog(request: schemas.BlogCreate, db: Session = Depends(database.get_db)):
    return blog.create(request, db)

# Delete Blog
@router.delete("/delete/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(id: int, db: Session = Depends(database.get_db)):
    return blog.delete(id, db)

# Update Blog
@router.put("/update/{id}", status_code=status.HTTP_200_OK)
def update_blog(id: int, request: schemas.BlogCreate, db: Session = Depends(database.get_db)):
   return blog.update(id, request, db)

# Get All Blogs
@router.get("/all", response_model=List[schemas.BlogRead])
def get_all_blogs(db: Session = Depends(database.get_db), current_user: schemas.UserRead = Depends(oAuth2.get_current_user)):
    return blog.get_all(db)

# Get Blog by ID
@router.get("/{id}", response_model=schemas.BlogRead)
def get_blog(id:int, response: Response, db: Session = Depends(database.get_db)):
    return blog.get_by_id(id, response, db)