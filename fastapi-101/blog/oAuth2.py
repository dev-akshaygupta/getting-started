from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from . import token

# Creates a dependency that handles OAuth2 token-based authentication
# Here URL is from where token will be fetched. In this case, we are using login module
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

# Validates the current user by verifying the provided OAuth2 Bearer token
def get_current_user(oauth_token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    return token.verify_token(oauth_token, credentials_exception)
