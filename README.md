# Employee Management System

A simple and responsive Employee Management System built using Python, Django, HTML, CSS, JavaScript, and SQLite. This application helps organizations manage employee records through an easy-to-use web interface.

---

## Features

- User Authentication (Login & Logout)
- Add New Employee
- Update Employee Details
- Delete Employee Records
- Search Employees
- View Employee List
- Responsive User Interface
- Django Admin Panel
- Static File Handling with WhiteNoise
- Render Deployment Ready

---

## Technologies Used

- Python 3
- Django
- HTML5
- CSS3
- JavaScript
- SQLite3
- WhiteNoise
- Gunicorn

---

## Project Structure

```
Employee-Management-System/
│
├── employee_management/
├── employees/
├── static/
├── templates/
├── db.sqlite3
├── manage.py
├── requirements.txt
├── build.sh
└── README.md
```

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/sudheersandepogu/Employee-Management-System.git
```

### Navigate to the Project

```bash
cd Employee-Management-System
```

### Create a Virtual Environment

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/macOS**

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Apply Migrations

```bash
python manage.py migrate
```

### Run the Development Server

```bash
python manage.py runserver
```

Open your browser and visit:

```
http://127.0.0.1:8000/
```

---

## Deployment

This project is configured for deployment on Render.

### Environment Variables

| Variable | Description |
|----------|-------------|
| DJANGO_SECRET_KEY | Django Secret Key |
| DJANGO_DEBUG | False |
| DJANGO_ALLOWED_HOSTS | Your Render Domain |

---

## Screenshots

You can add screenshots of the application in this section.

Example:

```
screenshots/
│── login.png
│── dashboard.png
│── employee_list.png
│── add_employee.png
```

---

## Future Enhancements

- Employee Profile Pictures
- Email Notifications
- Salary Management
- Attendance Tracking
- Department Management
- Payroll System
- Export Employee Data to PDF and Excel
- REST API Integration

---

## Author

**Sudheer Roy**

GitHub: https://github.com/sudheersandepogu

---

## License

This project is created for educational and learning purposes.
