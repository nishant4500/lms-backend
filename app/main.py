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

from app.routes import modules, enrollments, assignments, progress

app.include_router(auth.router)
app.include_router(courses.router)
app.include_router(modules.router)
app.include_router(enrollments.router)
app.include_router(assignments.router)
app.include_router(progress.router)