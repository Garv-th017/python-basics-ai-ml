import os
from contextlib import asynccontextmanager
from datetime import datetime, timedelta, timezone

import jwt

from bson import ObjectId
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pwdlib import PasswordHash

from database import client, users_collection
from models import UserCreate, UserLogin, UserResponse


# Load environment variables
load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM", "HS256")

security = HTTPBearer()

# Password hashing configuration
password_hash = PasswordHash.recommended()


# MongoDB connection setup
@asynccontextmanager
async def lifespan(app: FastAPI):

    await client.admin.command("ping")

    print("MongoDB connected successfully!")

    # Create unique email index
    await users_collection.create_index("email", unique=True)

    yield

    await client.close()


# Create FastAPI instance
app = FastAPI(lifespan=lifespan)


# Generate JWT token
def create_jwt_token(user_id: str):

    payload = {
        "sub": user_id,
        "exp": datetime.now(timezone.utc) + timedelta(minutes=30)
    }

    token = jwt.encode(
        payload,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return token


# Verify JWT token and get current user
async def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security)
):

    token = credentials.credentials

    try:

        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        user_id = payload.get("sub")

        if not user_id:
            raise HTTPException(
                status_code=401,
                detail="Invalid token"
            )

        user = await users_collection.find_one(
            {"_id": ObjectId(user_id)}
        )

        if not user:
            raise HTTPException(
                status_code=401,
                detail="User not found"
            )

        return user

    except (jwt.InvalidTokenError, ValueError):
        raise HTTPException(
            status_code=401,
            detail="Invalid or expired token"
        )


# Testing Route
@app.get("/")
async def health_route():

    return {
        "message": "FastAPI and MongoDB working successfully"
    }


# User Registration API
@app.post("/register", response_model=UserResponse)
async def register_user(data: UserCreate):

    # Check if user already exists
    existing_user = await users_collection.find_one(
        {"email": data.email}
    )

    if existing_user:
        raise HTTPException(
            status_code=409,
            detail="Email already registered"
        )

    # Hash the password
    hashed_password = password_hash.hash(data.password)

    # Create user document
    user_data = {
        "email": data.email,
        "password": hashed_password
    }

    # Insert user into MongoDB
    result = await users_collection.insert_one(user_data)

    return {
        "id": str(result.inserted_id),
        "email": data.email
    }


# User Login API
@app.post("/login")
async def user_login(data: UserLogin):

    # Find user using email
    user = await users_collection.find_one(
        {"email": data.email}
    )

    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    # Verify password
    is_password_valid = password_hash.verify(
        data.password,
        user["password"]
    )

    if not is_password_valid:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    # Generate JWT token
    token = create_jwt_token(str(user["_id"]))

    return {
        "access_token": token,
        "token_type": "bearer"
    }


# Protected Profile API
@app.get("/profile", response_model=UserResponse)
async def get_profile(
    user: dict = Depends(get_current_user)
):

    return {
        "id": str(user["_id"]),
        "email": user["email"]
    }