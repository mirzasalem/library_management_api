# Library Management System API

A RESTful API for managing a library system built with **Django** and **Django REST Framework (DRF)**.  
This system allows users to register, login, view books, rent and return books, while staff can manage the library's collection.

---

## Table of Contents

- [Features](#features)
- [Technologies](#technologies)
- [Installation](#installation)
- [API Endpoints](#api-endpoints)
- [Permissions](#permissions)
- [Models](#models)
- [Serializers](#serializers)
- [Usage](#usage)
- [Contributing](#contributing)

---

## Features

- User registration and login
- List all books
- Rent and return books for students
- Staff can add, update, and delete books
- Validation to ensure available copies do not exceed total copies
- Permission-based access for staff and students

---

## Technologies

- Python 3.x
- Django 5.0
- Django REST Framework
- MySQL
- JWT / DRF Token (optional for authentication)

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/mirzasalem/library_management_api
cd library-management
```

2. Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Apply migrations:

```bash
python manage.py migrate
```

5. Create a superuser (for staff):

```bash
python manage.py createsuperuser
```

6. Run the development server:

```bash
python manage.py runserver
```

Server will be running at: `http://127.0.0.1:8000/`

---

## API Endpoints

### Authentication

| Method | URL | Description |
| ------ | --- | ----------- |
| POST | `/register/` | Register a new user |
| POST | `/login/` | Login user (returns success message and user info) |

### Books

| Method | URL | Description |
| ------ | --- | ----------- |
| GET | `/index/` | List all books |
| GET | `/staff/` | Staff: list all books |
| POST | `/staff/` | Staff: Add a new book |
| GET | `/staff/<pk>/` | Staff: Retrieve book details |
| PUT | `/staff/<pk>/` | Staff: Update a book |
| PATCH | `/staff/<pk>/` | Staff: Partial update a book |
| DELETE | `/staff/<pk>/` | Staff: Delete a book |

### Rent / Return Books

| Method | URL | Description |
| ------ | --- | ----------- |
| POST | `/rent/<book_id>/` | Student: Rent a book |
| POST | `/return/<book_id>/` | Student: Return a book |

---

## Permissions

- **Students**
  - Can view books
  - Can rent and return books
- **Staff**
  - Can add, update, and delete books
  - Cannot rent or return books

---

## Models

### User
- Default Django user model
- Extended via `role` in serializer (student/staff)
- `is_staff` determines staff privileges

### Book
- `title` (string)
- `total_copies` (int)
- `available_copies` (int)

### Bookrent
- `user` (ForeignKey to User)
- `book` (ForeignKey to Book)
- `rented_at` (DateTime)
- `returned` (Boolean)

### Category
- `name` (string)
- Optional relation to books

---

## Serializers

- `RegisterSerializer` – Handles user registration with role
- `LoginSerializer` – Handles user login
- `BookSerializer` – List and retrieve books
- `AddBookSerializer` – Add/update books (staff)
- `CategorySerializer` – Serialize book categories

---

## Usage

1. Register a new user via `/register/`.
2. Login via `/login/` to authenticate.
3. Students can rent a book with `/rent/<book_id>/` and return via `/return/<book_id>/`.
4. Staff can manage books via `/staff/` endpoints.

---

## Contributing

Contributions are welcome!  

1. Fork the repository  
2. Create a new branch (`git checkout -b feature/your-feature`)  
3. Commit your changes (`git commit -am 'Add new feature'`)  
4. Push to the branch (`git push origin feature/your-feature`)  
5. Create a pull request

---


