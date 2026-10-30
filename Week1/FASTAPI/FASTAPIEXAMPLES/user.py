from fastapi import (
    FastAPI,
    HTTPException,
    Depends,
)  # basically this is required for the creation of the instance

from fastapi.security import (
    HTTPBearer,
    HTTPAuthorizationCredentials
)  # helps us extract the Bearer token

from pydantic import BaseModel
import jwt
from datetime import datetime, timedelta, timezone


# create an instance
app = FastAPI()

security = HTTPBearer()  # creating the scheme that helps us extract the token from the Authorization header


# Pydantic Basic User class types define
class UserBase(BaseModel):
    email: str
    password: str


# JWT configuration
SECRET_KEY = "user-Fast-api-Practice"
ALGORITHM = "HS256"


# Testing Route
@app.get("/")
def health_route():
    return {"message": "Health Route working successfully"}


# demo User credentials and here basically this is stored into the Dictionary with the normal Python dictionary with the inner layer

userData = {
    "garv@gmail.com": {
        "id": 1,
        "email": "garv@gmail.com",
        "password": "123456"
    }
}


# create jwt tokens example
def create_jwt_token(user_id: int):

    payload = {
        "sub": str(user_id),  # this is the subject and we convert the value to the string

        "exp": datetime.now(timezone.utc) + timedelta(minutes=30)
        # Here we are giving the expiration time basically current time + 30 minutes
    }

    token = jwt.encode(
        payload,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return token


# Verify JWT token
def verify_token(
    credentials: HTTPAuthorizationCredentials = Depends(security)
):
    # Here we pass our dependency injection. HTTPBearer helps us extract
    # the Bearer token from the Authorization header.

    token = credentials.credentials

    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        return payload

    except jwt.InvalidTokenError:
        raise HTTPException(
            status_code=401,
            detail="Invalid or expired token"
        )


# create the Login API
@app.post('/login')
def user_login(data: UserBase):
    # here we means that the data is the UserBase type

    user = userData.get(data.email)
    # here From the Demo data we are getting the user using the email we get from the API

    if not user or user["password"] != data.password:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    token = create_jwt_token(user["id"])

    return {
        "access_token": token,
        "token_type": "bearer"
    }


# Protected Profile API
@app.get("/profile")
def profile(
    payload: dict = Depends(verify_token)
):
    # Here we first verify and decode the token using verify_token.
    # If the token is invalid or expired, access is rejected.

    user_id = int(payload["sub"])

    return {
        "message": "Login successful",
        "user_id": user_id,
        "userDetail" : userData
    }
