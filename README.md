# Django Backend 📚

A Django-powered backend for managing authors and books, complete with user authentication, CRUD operations, and dynamic HTML rendering.

## Features
- 🔐 User login, logout, and registration
- 📖 Add, update, and delete books linked to authors
- 🧑‍💼 Create and list authors, with book count annotations
- 📥 File uploads with content handling
- 🎯 Auth-protected routes using `@login_required`

## Endpoints
- `/login/` – User login
- `/create/` – Register a new user
- `/author/` – Add authors
- `/post/` – Upload books tied to authors
- `/books/` – List all books (requires login)
- `/update/<id>/` – Edit book details
- `/delete/<id>/` – Delete a book (supports DELETE method)
- `/authors/` – List authors with book counts

## Setup
1. Clone the repo:
   ```bash
   git clone https://github.com/Parkerrei/django_backend.git
   cd django_backend

