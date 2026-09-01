# School Dashboard

Full-stack school management dashboard.

- **Backend**: Django REST Framework + PostgreSQL
- **Frontend**: React + TypeScript (Vite)

---

## Project Structure

```
test_amazon/
├── school-backend/    # Django DRF API
└── school-dashboard/  # React TypeScript frontend
```

---

## Backend Setup

### 1. Create and activate a virtual environment

```bash
cd school-backend
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure the database

Copy the example env file and fill in your PostgreSQL credentials:

```bash
cp .env.example .env
```

Edit `.env`:

```
DB_NAME=school_db
DB_USER=postgres
DB_PASSWORD=yourpassword
DB_HOST=localhost
DB_PORT=5432
```

Make sure your PostgreSQL server is running and the database exists:

```sql
CREATE DATABASE school_db;
```

### 4. Run migrations

```bash
python manage.py migrate
```

### 5. Seed sample data

```bash
python manage.py seed_data
```

This creates 5 departments, 10 teachers, and 15 students. Safe to run multiple times (idempotent).

### 6. (Optional) Create a superuser for Django Admin

```bash
python manage.py createsuperuser
```

### 7. Start the backend server

```bash
python manage.py runserver
```

**API base URL**: http://localhost:8000/api/

| Endpoint | Description |
|----------|-------------|
| `GET /api/departments/` | List all departments |
| `GET /api/teachers/` | List all teachers |
| `GET /api/students/` | List all students |
| `GET /api/teachers/?department=1` | Filter teachers by department |
| `GET /api/students/?grade=10th` | Filter students by grade |
| `GET /api/teachers/?search=alice` | Search teachers by name/email/subject |

Browsable API: http://localhost:8000/api/  
Django Admin: http://localhost:8000/admin/

---

## Frontend Setup

```bash
cd school-dashboard
npm install
```

### Run with live Django API

```bash
npm run dev
```

The `.env` file points to `http://localhost:8000/api` by default. Make sure the backend is running.

### Run with mock data (no backend needed)

```bash
# Temporarily use mock env
cp .env.mock .env.local
npm run dev
```

**Frontend URL**: http://localhost:5173

---

## Features

- **Overview tab**: Department cards showing teacher and student counts per department
- **Teachers tab**: Searchable, filterable table of all teachers
- **Students tab**: Searchable, filterable table with grade and department filters
- **Stats bar**: Live totals for departments, teachers, students, and student-to-teacher ratio
- **Refresh button**: Re-fetches all data from the API
