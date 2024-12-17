from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from .. import schemas, models, hashing

def login(request: schemas.Login, db: Session):
    user = db.query(models.User).filter(models.User.email==request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid Credentials!")
    
    if not hashing.Hash.verify(user.password, request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid Credentials!")
    return user