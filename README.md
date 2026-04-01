# 📚 LMS Backend (FastAPI)

A full-featured **Learning Management System (LMS) REST API** built with FastAPI. The backend supports user authentication, course management, module organization, student enrollments, assignment submission, and progress tracking.

---

## 👥 Contributors

| Name | Role |
|------|------|
| Nishanth Dwivedi | Backend Developer |
| Kashvi Sharma | Backend Developer |
| Jayanth Kumar Samatham | Backend Developer |

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Framework | [FastAPI](https://fastapi.tiangolo.com/) |
| ORM | [SQLAlchemy](https://www.sqlalchemy.org/) |
| Database | SQLite |
| Validation | [Pydantic](https://docs.pydantic.dev/) |
| Authentication | JWT (`python-jose`) + password hashing (`passlib`) |
| Server | [Uvicorn](https://www.uvicorn.org/) |

---

## 📂 Project Structure

```
lms-backend/
├── app/
│   ├── main.py          # FastAPI app entry point; router registration
│   ├── database.py      # SQLAlchemy engine & session setup
│   ├── models.py        # ORM table definitions
│   ├── schemas.py       # Pydantic request/response schemas
│   ├── crud.py          # Database CRUD helpers
│   ├── deps.py          # Dependency injection (current user, DB session)
│   ├── security.py      # JWT creation & password utilities
│   └── routes/
│       ├── auth.py          # /register, /login
│       ├── courses.py       # Course CRUD
│       ├── modules.py       # Module CRUD
│       ├── enrollments.py   # Student enrolment
│       ├── assignments.py   # Assignment creation & submission
│       └── progress.py      # Student progress retrieval
├── postman/
│   └── lms-api-collection.json   # Ready-to-import Postman collection
├── tests/
│   ├── test_auth.py
│   ├── test_courses.py
│   ├── test_modules.py
│   ├── test_enrollment.py
│   └── test_assignment.py
├── Dockerfile
├── requirements.txt
└── README.md
```

---

## 🔄 Project Flow

```
1. Register / Login  →  receive JWT access token
2. Instructor creates Courses  →  adds Modules and Assignments to each course
3. Student enrolls in a Course  →  accesses Modules
4. Student submits Assignments  →  progress is tracked
5. Progress endpoint returns completion status per student
```

> All protected endpoints require the `Authorization: Bearer <token>` header.

---

## ⚙️ Setup & Run

### Prerequisites

* Python 3.9+
* `pip`

### 1. Clone the repository

```bash
git clone https://github.com/nishant4500/lms-backend.git
cd lms-backend
```

### 2. Create and activate a virtual environment

```bash
# Linux / macOS
python -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the development server

```bash
uvicorn app.main:app --reload
```

The API will be available at `http://127.0.0.1:8000`.  
Interactive docs: `http://127.0.0.1:8000/docs`

### 5. Run with Docker (optional)

```bash
docker build -t lms-backend .
docker run -p 8000:8000 lms-backend
```

### 6. Run tests

```bash
pytest tests/
```

---

## 📌 API Endpoints

### 🔐 Authentication

| Method | Endpoint | Description | Auth required |
|--------|----------|-------------|---------------|
| `POST` | `/register` | Register a new user | ❌ |
| `POST` | `/login` | Login and receive a JWT token | ❌ |

### 📚 Courses

| Method | Endpoint | Description | Auth required |
|--------|----------|-------------|---------------|
| `POST` | `/courses` | Create a new course | ✅ Instructor |
| `GET` | `/courses` | List all courses | ✅ |
| `PUT` | `/courses/{course_id}` | Update course details | ✅ Instructor |
| `DELETE` | `/courses/{course_id}` | Delete a course | ✅ Instructor |

### 🗂️ Modules

| Method | Endpoint | Description | Auth required |
|--------|----------|-------------|---------------|
| `POST` | `/modules` | Add a module to a course | ✅ Instructor |
| `GET` | `/modules/{course_id}` | Get all modules for a course | ✅ |

### 🎓 Enrollments

| Method | Endpoint | Description | Auth required |
|--------|----------|-------------|---------------|
| `POST` | `/courses/{id}/enroll` | Enroll a student in a course | ✅ Student |

### 📝 Assignments

| Method | Endpoint | Description | Auth required |
|--------|----------|-------------|---------------|
| `POST` | `/assignments` | Create an assignment | ✅ Instructor |
| `POST` | `/assignments/{id}/submit` | Submit an assignment | ✅ Student |

### 📊 Progress

| Method | Endpoint | Description | Auth required |
|--------|----------|-------------|---------------|
| `GET` | `/progress/{student_id}` | Get progress for a student | ✅ |

---

## 🗂️ Postman Collection

A pre-built Postman collection is available at `postman/lms-api-collection.json`.  
Import it directly into Postman to explore and test all endpoints without manual setup.

---

## 📝 Notes

* The SQLite database file (`lms.db`) is auto-created on first run — no manual setup required.
* The virtual environment (`venv/`) is excluded from version control.
* JWT tokens expire after a configurable period; update the secret key and expiry in `app/security.py` before deploying to production.
* For production use, replace SQLite with a production-grade database (e.g. PostgreSQL) and set a strong `SECRET_KEY` via environment variables.
