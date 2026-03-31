from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    email: str
    password: str
    role: str


class UserLogin(BaseModel):
    email: str
    password: str


class CourseCreate(BaseModel):
    title: str
    description: str

class ModuleCreate(BaseModel):
    title: str
    content: str
    course_id: int

class EnrollmentCreate(BaseModel):
    course_id: int

class AssignmentCreate(BaseModel):
    title: str
    description: str
    course_id: int

class SubmissionCreate(BaseModel):
    content: str