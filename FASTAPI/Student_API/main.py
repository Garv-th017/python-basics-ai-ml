from fastapi import FastAPI
from routers import user

app = FastAPI()  # create the fastapi instance 
app.include_router(user.router)

@app.get('/')
def healthy_route():
    return {
        "Message" : "Healthy Route"
    }
