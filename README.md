# 📚 Book Library API

A simple REST API built with **FastAPI, SQLite, and SQLAlchemy** for managing a book library.

This project was built to practice backend development concepts including CRUD operations, database integration, validation, filtering, pagination, sorting, and error handling.

## 🚀 Features

- Create a book
- Get all books
- Get a single book
- Update a book
- Delete a book
- Filter books by:
  - Category
  - Author
  - Availability
- Pagination using `skip` and `limit`
- Sort books by title or published year
- Request validation using Pydantic
- SQLite database with SQLAlchemy
- Proper 404 error handling
- Response models

## 🛠️ Tech Stack

- Python
- FastAPI
- Pydantic
- SQLAlchemy
- SQLite
- Uvicorn
- Postman
- Git & GitHub

## 📁 Project Structure

```text
book_library/
│
├── main.py
├── database.py
├── models.py
├── schemas.py
├── requirements.txt
├── .gitignore
├── books.db
└── README.md