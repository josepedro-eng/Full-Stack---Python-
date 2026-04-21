# Task Manager API - Backend Focused Project

## About the Project

This project is a **Task Manager API** developed with the main focus on **backend development**, using RESTful API principles and database integration.

The goal of this project was to practice and demonstrate skills in:

* Backend development
* REST API design
* Database modeling
* ORM usage
* CRUD operations
* Relationship between entities

The frontend included in this project was created only for basic testing purposes, and **it was not the main focus**, since the primary objective was to build a solid backend structure.

---

## Technologies Used

* **Python**
* **FastAPI** — REST API framework
* **SQLAlchemy** — ORM for database management
* **PostgreSQL** — Relational database
* **Uvicorn** — ASGI server
* **Pydantic** — Data validation

---

## Project Structure

```
project/
│
├── database.py       # Database connection configuration
├── models.py         # Database models (Usuario and Tarefa)
├── schemas.py        # Data validation schemas
├── crud.py           # CRUD operations
├── main.py           # API routes
└── create_db.py      # Script to create database tables
```

---

## Database Design

This project uses **relational database modeling**, with two main entities:

### Usuario

* id
* nome
* email

### Tarefa

* id
* titulo
* descricao
* usuario_id (Foreign Key)

Relationship:

* **One Usuario → Many Tarefas**

---

##  API Features

The API supports basic CRUD operations:

### Usuario

* Create user
* List users

### Tarefa

* Create task
* List tasks

---

## Project Objective

The main objective of this project was to **strengthen backend development skills**, focusing on:

* REST API architecture
* Database integration
* ORM usage
* Backend logic organization
* Clean project structure

The frontend part is simple and was created only to interact with the API, since the **core focus of this project is backend development**.

---

## Future Improvements

Possible enhancements for this project:

* User authentication (JWT)
* Update and delete operations
* Task status management
* Filtering tasks by user
* Pagination support
* Frontend improvement

---

## Author

Developed by **José Pedro**

Software Engineering Student
Backend Developer in training 🚀
