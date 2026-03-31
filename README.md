# 📚 LMS Backend (FastAPI)

## 🚀 Project Overview

This is a Learning Management System (LMS) backend built using FastAPI.
It allows users to register, login, and manage courses.

---

## 🛠️ Tech Stack

* FastAPI
* SQLAlchemy
* SQLite
* Pydantic
* Uvicorn

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/nishant4500/lms-backend.git
cd lms-backend

```

### 2. Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the server

```bash
uvicorn app.main:app --reload
```

---

## 📌 API Endpoints

### 🔐 Authentication

* POST /register → Register user
* POST /login → Login user

### 📚 Courses

* GET /courses → Get all courses
* POST /courses → Create course
* PUT /courses/{course_id} → Update course
* DELETE /courses/{course_id} → Delete course

---

```
Bearer <your_token>
```

---

## 📂 Project Structure

```
lms_backend/
│── app/
│   │── main.py
│   │── database.py
│   │── models.py
│   │── schemas.py
│   │── routes/
│       │── auth.py
│       │── courses.py
│── requirements.txt
│── README.md
```

---

## 👨‍💻 Author

Nishant Dwivedi

---

## 📌 Notes

* SQLite database (`lms.db`) is auto-created
* Virtual environment (`venv`) is not included in repo
