Reminder App
A Django-based reminder application that allows users to set reminders with custom messages, scheduled times, and recurring frequencies.
The app automatically delivers reminders at the specified time using Celery Beat for task scheduling.

Features
Create reminders with custom messages
Schedule reminders for specific times
Set reminder frequency (once, daily, weekly)
Automatic reminder delivery via Celery Beat
JWT-based authentication
RESTful API

API Endpoints

Authentication
POST /auth/users/ - User registration
POST /auth/jwt/create/ - Login (get JWT token)
POST /auth/jwt/refresh/ - Refresh JWT token
GET /auth/users/me/ - Get current user info

Reminders
GET /reminder/ - List all user reminders
POST /reminder/ - Create a new reminder
GET /reminder/{id}/ - Get specific reminder
PUT /reminder/{id}/ - Update reminder
DELETE /reminder/{id}/ - Delete reminder

Setup
Install dependencies:
bash poetry install

Run migrations:
bash python manage.py migrate

Start Redis server:
bash redis-server

Start celery worker:
bash celery -A task_scheduler worker --loglevel=info

Start celery Beat scheduler:
bash celery -A task_scheduler beat --loglevel=info

Run Django development server:
bash python manage.py runserver
Usage

Register a user account via /auth/users/
Login to get JWT token via /auth/jwt/create/
Include token in Authorization header: Authorization: JWT <your-token>
Create reminders via /reminder/ with:

message: Reminder text
remind_at: Datetime when to send reminder (format: YYYY-MM-DDTHH:MM:SS)
frequency: Choose from once, daily, or weekly



How It Works

Celery Beat runs every minute checking for due reminders
When a reminder's remind_at time arrives, it's sent to the user
Once: Reminder is deleted after delivery
Daily: Reminder is rescheduled for next day
Weekly: Reminder is rescheduled for next week

Example Request
bash curl -X POST http://localhost:8000/reminder/ \
  -H "Authorization: JWT <your-token>" \
  -H "Content-Type: application/json" \
  -d '{
    "message": "Take your medication",
    "remind_at": "2025-12-09T14:30:00",
    "frequency": "daily"
  }'