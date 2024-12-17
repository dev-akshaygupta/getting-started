from fastapi import HTTPException, status, Depends, Response
from sqlalchemy.orm import Session
from .. import schemas, models, hashing, token
from fastapi.security import OAuth2PasswordRequestForm
from ..repository import user

def login(db: Session, response: Response, request: OAuth2PasswordRequestForm = Depends()):
    get_user = user.get_user_by_email(request, response, db)
    if not get_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid Credentials!")
    
    if not hashing.Hash.verify(get_user.password, request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid Credentials!")
    
    access_token = token.create_access_token(
        data={"sub": get_user.email} 
    )
    return schemas.Token(access_token=access_token, token_type="bearer")