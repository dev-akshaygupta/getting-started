from fastapi import APIRouter, Depends, HTTPException, status, Response
from .. import schemas, models, database, hashing
from sqlalchemy.orm import Session
from sqlmodel import select
from typing import List

router = APIRouter(
    prefix="/v1/user",
    tags=["Users"]
)

# Create User
@router.post("/create", status_code=status.HTTP_201_CREATED)
def create_user(request: schemas.UserCreate, db: Session = Depends(database.get_db)):
    new_user = models.User(name=request.name, email=request.email, password=hashing.Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user 

# Get All Users
@router.get("/all", response_model=List[schemas.UserRead])
def get_all_users(db: Session = Depends(database.get_db)):
    get_user = select(models.User)
    result = db.exec(get_user).all()
    return result

# Get User by ID
@router.get("/{id}", response_model=schemas.UserRead)
def get_all_users(id:int, response: Response, db: Session = Depends(database.get_db)):
    get_user = select(models.User).where(models.User.id == id)
    result = db.exec(get_user).one_or_none()
    if not result:
        response.status_code = status.HTTP_404_NOT_FOUND
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found!")
    return result