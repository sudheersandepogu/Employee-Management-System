# Employee Management System

A Django-based employee management system with an attractive Bootstrap UI and a unique employee model.

## Setup

1. Create a virtual environment:
   ```bash
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Apply migrations:
   ```bash
   python manage.py migrate
   ```
4. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```
5. Run the development server:
   ```bash
   python manage.py runserver
   ```

## Features

- Login system for admin users
- Add, update, delete, and search employee records
- Modern dashboard with employee statistics
- Custom employee model with department, role, status, and notes

## Notes

- The project uses SQLite by default. To use MySQL, update `DATABASES` in `employee_management/settings.py`.
