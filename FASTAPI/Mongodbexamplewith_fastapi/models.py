from pydantic import BaseModel

# User Registration Model
class UserCreate(BaseModel):
    email: str
    password: str


# User Login Model
class UserLogin(BaseModel):
    email: str
    password: str


# User Response Model
class UserResponse(BaseModel):
    id: str
    email: str