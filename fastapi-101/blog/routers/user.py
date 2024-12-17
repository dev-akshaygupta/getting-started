from fastapi import APIRouter, Depends, status, Response
from .. import schemas, database
from sqlalchemy.orm import Session
from typing import List
from ..repository import user

router = APIRouter(
    prefix="/v1/user",
    tags=["Users"]
)

# Create User
@router.post("/create", status_code=status.HTTP_201_CREATED)
def create_user(request: schemas.UserCreate, db: Session = Depends(database.get_db)):
    return user.create(request, db)

# Get All Users
@router.get("/all", response_model=List[schemas.UserRead])
def get_all_users(db: Session = Depends(database.get_db)):
    return user.get_all(db)

# Get User by ID
@router.get("/{id}", response_model=schemas.UserRead)
def get_all_users(id:int, response: Response, db: Session = Depends(database.get_db)):
    return user.get_by_id(id, response, db)