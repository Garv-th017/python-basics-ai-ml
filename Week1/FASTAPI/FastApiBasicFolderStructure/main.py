
from fastapi import FastAPI
from routers import user

app = FastAPI(
    title="My FastAPI Project",
    version="1.0.0"
)

app.include_router(user.router)

@app.get("/")
def home():
    return {"message": "Welcome to my FastAPI application"}
