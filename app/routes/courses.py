from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app import models, schemas

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/courses")
def create_course(course: schemas.CourseCreate, db: Session = Depends(get_db)):
    new_course = models.Course(
        title=course.title,
        description=course.description,
        instructor_id=1  # temp
    )
    db.add(new_course)
    db.commit()
    return {"msg": "Course created"}


@router.get("/courses")
def get_courses(db: Session = Depends(get_db)):
    return db.query(models.Course).all()

@router.put("/courses/{course_id}")
def update_course(course_id: int, course: schemas.CourseCreate, db: Session = Depends(get_db)):
    db_course = db.query(models.Course).filter(models.Course.id == course_id).first()

    if not db_course:
        return {"error": "Course not found"}

    db_course.title = course.title
    db_course.description = course.description

    db.commit()
    return {"msg": "Course updated"}

@router.delete("/courses/{course_id}")
def delete_course(course_id: int, db: Session = Depends(get_db)):
    db_course = db.query(models.Course).filter(models.Course.id == course_id).first()

    if not db_course:
        return {"error": "Course not found"}

    db.delete(db_course)
    db.commit()
    return {"msg": "Course deleted"}