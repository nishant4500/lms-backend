from sqlalchemy.orm import Session
from app import models, schemas


def create_course(db: Session, course: schemas.CourseCreate):
    new_course = models.Course(
        title=course.title,
        description=course.description,
        instructor_id=1
    )
    db.add(new_course)
    db.commit()
    db.refresh(new_course)
    return new_course


def get_courses(db: Session):
    return db.query(models.Course).all()


def update_course(db: Session, course_id: int, course: schemas.CourseCreate):
    db_course = db.query(models.Course).filter(models.Course.id == course_id).first()
    
    if not db_course:
        return None

    db_course.title = course.title
    db_course.description = course.description
    db.commit()
    return db_course


def delete_course(db: Session, course_id: int):
    db_course = db.query(models.Course).filter(models.Course.id == course_id).first()

    if not db_course:
        return None

    db.delete(db_course)
    db.commit()
    return db_course