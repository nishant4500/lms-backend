from fastapi import FastAPI
from app.database import engine
from app import models
from app.routes import auth
from app.routes import courses


# CREATE TABLES
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def root():
    return {"message": "LMS running"}

app.include_router(auth.router)

app.include_router(courses.router)