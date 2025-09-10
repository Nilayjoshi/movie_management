from fastapi import FastAPI
from .routes import router

app = FastAPI(
    title="Movie Management",
    description="Movie CRUD API's",
    version="0.0.1"
)

app.include_router(router)
