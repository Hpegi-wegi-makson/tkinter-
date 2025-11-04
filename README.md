🛠️ Service Desk Management System
Desktop application for managing technical support requests, built with Python using Tkinter and SQLite.

🏗️ Project Architecture
Technology Stack:
Frontend: Tkinter (GUI framework)

Backend: Python 3.x

Database: SQLite 3

Data Access: SQLite3 connector

📊 Database Schema
User Table
sql
CREATE TABLE User (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    login TEXT UNIQUE,
    password TEXT,
    fio TEXT,
    role TEXT
)
Request Table
sql
CREATE TABLE Request (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    data TEXT,
    broken_devices TEXT,
    problem_description TEXT,
    status_request TEXT,
    fio_client TEXT
)
🔐 Authentication & Role System
User Roles:
Admin: Full system access

User: Limited access (create and view requests only)

Default Admin Account:
python
login: "admin"
password: "admin_pass"
role: "admin"
📋 Core Features
1. Authentication Module
User credential validation

Role-based routing

Session management

2. Request Management
Create new support requests

Equipment selection (Mouse, Keyboard, System Unit, Monitor, Internet)

Problem description

Status tracking ("pending", "in progress", "completed")

View all requests with scrollable interface

3. User Management (Admin only)
Create new users

View user list

Role assignment

🗃️ Data Models
Request Entity:
data: Creation timestamp (auto-generated)

broken_devices: List of malfunctioning equipment

problem_description: Detailed issue description

status_request: Current request status

fio_client: Client full name

User Entity:
login: Unique identifier

password: User password (plaintext - needs improvement)

fio: Full name

role: System role

🚀 Installation & Usage
bash
python main.py
🔧 Requirements
Python 3.6+

tkinter (usually included with Python standard library)

sqlite3 (built-in Python module)

⚡ Implementation Notes
Current Strengths:
Clear role-based interface separation

Automatic database initialization

Intuitive GUI design

Full CRUD operations for requests

Recommended Backend Improvements:
Security Enhancements:

Password hashing (bcrypt, hashlib)

Comprehensive SQL injection protection (use parameterized queries exclusively)

Architecture Refactoring:

Extract database logic into separate Data Access Layer

Implement Repository pattern for entity management

Add business logic validation layer

Database Optimization:

Add indexes on frequently queried fields

Implement foreign keys and proper table relationships

Data normalization

Operational Excellence:

Comprehensive logging system

Structured exception handling

Input validation and sanitization

💡 Database API Examples
python
# Create new request
cursor.execute(
    "INSERT INTO Request (data, broken_devices, problem_description, status_request, fio_client) VALUES (?,?,?,?,?)",
    (datetime, devices, description, status, fio)
)

# User authentication
cursor.execute(
    "SELECT login, password FROM User WHERE login = ? AND password = ?",
    (username, password)
)

# Get all requests
cursor.execute('''
    SELECT data, broken_devices, problem_description, status_request, fio_client 
    FROM Request
''')
🎯 Usage Flow
Launch application → Auto-creates database with default admin

1 - Login with credentials (admin/user)

2 - Role-based dashboard loads

3 - Create/view requests based on permissions

4 - Admin features: User management and full request access

