from fastapi import APIRouter, Depends
from .. import schemas, database
from sqlalchemy.orm import Session
from ..repository import authentication

router =  APIRouter(
    prefix="/auth",
    tags=["Auth"]
)

@router.post("/login")
def login(request: schemas.Login, db: Session = Depends(database.get_db)):
    return authentication.login(request, db)