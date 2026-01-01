from fastapi import HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
import bcrypt
from random import randint


SECRET_KEY = "This is my secret key"
ALGORITHM = "HS256"

# it used to get the token from the request header
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login") 


def create_token(data: dict):
    return jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)

# it used to get the current user from the token
def get_current_user(token: str = Depends(oauth2_scheme)): # Depends is used to get the token from the request header
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email = payload.get("sub")
        if email is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    raise credentials_exception




def hashed_password(plain: str) -> str:
    return bcrypt.hashpw(
        plain.encode("utf-8"),
        bcrypt.gensalt()).decode("utf-8")


def verify_password(plain: str, hashed: str) -> bool:
    try:
        return bcrypt.checkpw(
            plain.encode("utf-8"),
            hashed.encode("utf-8"))
    except Exception as exp:
        return exp




def gen_otp():
    otp = randint(100000, 999999)
    return otp
