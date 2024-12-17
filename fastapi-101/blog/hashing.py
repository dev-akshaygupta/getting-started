from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Hash():
    # Encrypt Password
    def bcrypt(password: str):
        return pwd_context.hash(password)
    
    # Verify Password
    def verify(user_password: str, req_password: str):
        return pwd_context.verify(req_password, user_password)