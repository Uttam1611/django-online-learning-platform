<!-- PROJECT LOGO -->
<br />
<div align="center">
  <h3 align="center">Django Online Learning Platform</h3>
  <p align="center">
    A beginner-friendly backend for an educational platform with course management, user progress tracking, and quizzes.
    <br />
    <a href="https://github.com/yourusername/django-online-learning-platform"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/yourusername/django-online-learning-platform/issues">Report Bug</a>
    ·
    <a href="https://github.com/yourusername/django-online-learning-platform/issues">Request Feature</a>
  </p>
</div>

---

## 📚 About The Project

This project is a Django backend for an online learning platform.  
It supports course management, user enrollment, progress tracking, and quiz administration.  
Built with Django, Django Channels (for real-time features), and PostgreSQL.

---

### 🛠️ Built With

- [Django](https://www.djangoproject.com/)
- [Django Channels](https://channels.readthedocs.io/en/latest/)
- [PostgreSQL](https://www.postgresql.org/)
- [Redis](https://redis.io/) (for real-time features)
- [Python 3.11+](https://www.python.org/)

---

## 🚀 Features

- Instructor and student roles
- Course creation, update, and enrollment
- Quiz creation, participation, and scoring
- Student progress tracking
- Real-time updates with Django Channels + Redis
- Admin interface for easy management

---

## 📦 Getting Started

### Prerequisites

- Python 3.11+
- PostgreSQL
- Redis (optional, for Channels)
- Git

### Installation

1. **Clone the repo**

   ```bash
   git clone https://github.com/yourusername/django-online-learning-platform.git
   cd django-online-learning-platform/backend
   ```

2. **Create and activate a virtual environment**

   ```bash
   python -m venv venv
   venv\Scripts\activate  # On Windows
   # source venv/bin/activate  # On Linux/Mac
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure PostgreSQL**

   Edit `backend/settings.py` with your DB credentials:

   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': 'coursedb',
           'USER': 'postgres',
           'PASSWORD': 'yourpassword',
           'HOST': 'localhost',
           'PORT': '5432',
       }
   }
   ```

5. **Run migrations**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create a superuser**

   ```bash
   python manage.py createsuperuser
   ```

7. **Collect static files**

   ```bash
   python manage.py collectstatic
   ```

8. **Run the development server**
   ```bash
   python manage.py runserver
   ```
   Or, for Channels/ASGI:
   ```bash
   uvicorn backend.asgi:application --reload
   ```

---

## 🧪 Running Tests

```bash
python manage.py test
```

---

## 📋 Usage

- Access the admin panel at `http://127.0.0.1:8000/admin/` to manage courses, quizzes, and users.
- Students can enroll in courses and take quizzes from the main site.

---

## 🗂️ Project Structure

```
backend/
├── core/
│   ├── admin.py
│   ├── models.py
│   ├── views.py
│   ├── tests.py
│   └── templates/core/
├── backend/
│   ├── settings.py
│   ├── urls.py
│   └── asgi.py
├── manage.py
└── requirements.txt
```

---

## 🤝 Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create.  
Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

---

## 🙏 Acknowledgments

- [Django Documentation](https://docs.djangoproject.com/)
- [Best-README-Template](https://github.com/othneildrew/Best-README-Template)
- [Channels Documentation](https://channels.readthedocs.io/en/latest/)
