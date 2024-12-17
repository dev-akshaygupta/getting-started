from fastapi import HTTPException, status, Response
from .. import models, schemas
from sqlmodel import select
from sqlalchemy.orm import Session

def create(request: schemas.BlogCreate, db: Session):
    new_blog = models.Blog(title=request.title, body=request.body, creator_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def delete(id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found!")
    blog.delete(synchronize_session=False)
    db.commit()
    return {'Blog is deleted successfully!'}

def update(id: int, request: schemas.BlogCreate, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found!")
    blog.sqlmodel_update(request)
    db.commit()
    db.refresh(blog)
    return blog

def get_all(db: Session):
    get_blogs = select(models.Blog)
    result = db.exec(get_blogs).all()
    return result

def get_by_id(id: int, response: Response, db: Session):
    get_blog = select(models.Blog).where(models.Blog.id == id)
    result = db.exec(get_blog).one_or_none()
    if not result:
        response.status_code = status.HTTP_404_NOT_FOUND
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found!")
    return result