# 🎓 IELTS Speaking Test Backend

This project is the backend implementation for the **IELTS Speaking Test Platform**, developed as part of the Edubot PFSD React + Flask course.

It includes:
- SQLAlchemy models for users and test records (Assignment 9)

### ✅ Assignment 9: Develop the Database Models

- Implemented SQLAlchemy models:
  - `User`: Stores user info
  - `SpeakingTest`: Stores speaking test records
  - `ListeningTest`: Stores listening test records
- Defined relationships and foreign keys
- Added full CRUD operations for all models
- Validated via `test_crud.py`

- ## ⚙️ How to Run

### 1. Clone and Setup

```bash
git clone https://github.com/your-username/assignment9-backend.git
cd assignment9-backend
python -m venv venv
venv\Scripts\activate   # On Windows
pip install -r requirements.txt

python app.py
This starts the backend server on:
📍 http://localhost:5000

A. Test Model CRUD Operations (Assignment 9)
Run:

bash
Copy
Edit
python test_crud.py

📚 Technologies Used
Python 3.x

Flask

Flask-SQLAlchemy

Flask-Migrate

SQLite (can switch to MySQL/PostgreSQL)
