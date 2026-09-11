# Student Management API

A RESTful API for managing student records, built with **Python, FastAPI, SQLAlchemy, and MySQL**.

## Features

* Create, read, update, and delete student records
* Search students by name or email
* Filter students by age and active status
* Pagination for student listings
* Input validation using Pydantic
* MySQL database integration using SQLAlchemy
* API health check endpoint
* Automated API testing with Pytest
* Interactive API documentation with Swagger UI

## Tech Stack

* **Python**
* **FastAPI**
* **SQLAlchemy**
* **MySQL**
* **PyMySQL**
* **Pydantic**
* **Pytest**
* **Uvicorn**
* **Git**

## Project Structure

```text
student-management-api/
│
├── app/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── crud.py
│   └── routers/
│       ├── students.py
│       └── health.py
│
├── tests/
│   └── test_students.py
│
├── sql/
│   └── student_management.sql
│
├── .env.example
├── requirements.txt
├── README.md
└── .gitignore
```

## Module Overview

### `main.py`

Initializes the FastAPI application and registers the API routers.

### `database.py`

Creates and manages the MySQL database connection and SQLAlchemy sessions.

### `models.py`

Defines the SQLAlchemy database models, including the `Student` model.

### `schemas.py`

Defines request and response schemas and handles input validation using Pydantic.

### `crud.py`

Contains database operations for creating, retrieving, updating, and deleting student records, along with search, filtering, and pagination logic.

### `routers/students.py`

Defines the REST API endpoints for student management.

### `routers/health.py`

Provides a health-check endpoint to verify that the API and database connection are working correctly.

### `tests/test_students.py`

Contains automated tests for the API endpoints and validation logic.

## Installation

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd student-management-api
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

On Windows:

```bash
.venv\Scripts\activate
```

On macOS/Linux:

```bash
source .venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

## MySQL Configuration

Create the database and `students` table using the SQL script:

```text
sql/student_management.sql
```

You can run the script using MySQL Workbench or the MySQL command line.

## Environment Variables

Create a `.env` file based on `.env.example`.

Example:

```env
DATABASE_URL=mysql+pymysql://root:your_password@localhost:3306/student_management
```

Replace `your_password` with your actual MySQL password.

> Do not commit your `.env` file to GitHub because it may contain sensitive database credentials.

## Running the Application

Start the FastAPI server using Uvicorn:

```bash
uvicorn app.main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

Interactive Swagger documentation:

```text
http://127.0.0.1:8000/docs
```

## API Endpoints

| Method | Endpoint           | Description                           |
| ------ | ------------------ | ------------------------------------- |
| GET    | `/health`          | Check API and database health         |
| GET    | `/students`        | Get all students                      |
| GET    | `/students/search` | Search, filter, and paginate students |
| GET    | `/students/{id}`   | Get a student by ID                   |
| POST   | `/students`        | Create a new student                  |
| PUT    | `/students/{id}`   | Update a student's complete record    |
| PATCH  | `/students/{id}`   | Partially update a student            |
| DELETE | `/students/{id}`   | Delete a student                      |

## Search, Filtering & Pagination

Example request:

```text
GET /students/search?keyword=An&min_age=18&max_age=25&is_active=true&page=1&page_size=10
```

Supported parameters:

* `keyword` — Search by student name or email
* `min_age` — Minimum age
* `max_age` — Maximum age
* `is_active` — Filter by active status
* `page` — Page number
* `page_size` — Number of records per page

## Validation

The API validates incoming data, including:

* Student name cannot be empty
* Email must have a valid format
* Email must be unique
* Phone number must be unique
* Password must contain at least 6 characters
* Age must be between 1 and 120
* Page number must be at least 1
* Page size must be between 1 and 100
* Minimum age cannot be greater than maximum age

## Testing

Run the test suite with:

```bash
pytest -v
```

The project includes tests covering:

1. Health check
2. Student listing
3. Get student by ID
4. Non-existent student
5. Create student
6. Duplicate email validation
7. Input validation
8. PUT update
9. PATCH update
10. Delete student
11. Search, filtering, and pagination
12. Invalid pagination

## Future Improvements

Possible improvements include:

* JWT authentication and authorization
* Password hashing
* Docker support
* AWS deployment
* API rate limiting
* Alembic database migrations
* Improved logging and monitoring
