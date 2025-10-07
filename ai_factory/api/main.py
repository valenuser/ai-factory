from fastapi import FastAPI
import uvicorn
from .router import models, health


app = FastAPI()


app.include_router(models.router, prefix="/models", tags=["models"])
app.include_router(health.router, prefix="/health", tags=["health"])


@app.get("/")
def read_root():
    return {"message": "Welcome to the AI Model Management API!"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)