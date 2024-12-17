from fastapi import HTTPException, status, Response
from .. import schemas, models, hashing
from sqlalchemy.orm import Session
from sqlmodel import select

def create(request: schemas.UserCreate, db: Session):
    new_user = models.User(name=request.name, email=request.email, password=hashing.Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_all(db: Session):
    get_user = select(models.User)
    result = db.exec(get_user).all()
    return result

def get_by_id(id: int, response: Response, db: Session):
    get_user = select(models.User).where(models.User.id == id)
    result = db.exec(get_user).one_or_none()
    if not result:
        response.status_code = status.HTTP_404_NOT_FOUND
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found!")
    return result