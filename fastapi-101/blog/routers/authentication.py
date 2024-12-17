from fastapi import APIRouter, Depends, Response
from fastapi.security import OAuth2PasswordRequestForm
from .. import schemas, database
from sqlalchemy.orm import Session
from ..repository import authentication

router =  APIRouter(
    tags=["Auth"]
)

@router.post("/login")
def login(request: OAuth2PasswordRequestForm = Depends(), response = Response, db: Session = Depends(database.get_db)):
    return authentication.login(db, response, request)