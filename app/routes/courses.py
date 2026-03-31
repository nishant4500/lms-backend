from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app import schemas, crud

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# CREATE
@router.post("/courses")
def create_course(course: schemas.CourseCreate, db: Session = Depends(get_db)):
    return crud.create_course(db, course)


# READ
@router.get("/courses")
def get_courses(db: Session = Depends(get_db)):
    return crud.get_courses(db)


# UPDATE
@router.put("/courses/{course_id}")
def update_course(course_id: int, course: schemas.CourseCreate, db: Session = Depends(get_db)):
    updated_course = crud.update_course(db, course_id, course)

    if not updated_course:
        raise HTTPException(status_code=404, detail="Course not found")

    return {"msg": "Course updated"}


# DELETE
@router.delete("/courses/{course_id}")
def delete_course(course_id: int, db: Session = Depends(get_db)):
    deleted_course = crud.delete_course(db, course_id)

    if not deleted_course:
        raise HTTPException(status_code=404, detail="Course not found")

    return {"msg": "Course deleted"}