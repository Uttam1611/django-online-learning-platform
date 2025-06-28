# Django Online Learning Platform

A beginner-friendly Django backend for an online learning platform.  
Features include course management, user enrollment, progress tracking, and quiz administration.  
Built with Django, Django Channels (for real-time features), and Redis support.  
Now configured for PostgreSQL as the database backend.

---

## Features

- Instructor and student roles
- Course creation and enrollment
- Quiz creation, participation, and scoring
- Student progress tracking
- Real-time capabilities with Django Channels + Redis

---

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/django-online-learning-platform.git
cd django-online-learning-platform/backend
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
venv\Scripts\activate  # On Windows
# source venv/bin/activate  # On Linux/Mac
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure PostgreSQL

Edit `backend/settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### 5. Run migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create a superuser

```bash
python manage.py createsuperuser
```

### 7. Run the development server

```bash
python manage.py runserver
```

Or, for Channels/ASGI:

```bash
uvicorn backend.asgi:application --reload
```

---

## Testing

Run all automated tests:

```bash
python manage.py test
```

---

## License

MIT License

---

## Credits

Built with Django, Django Channels, and Redis.
