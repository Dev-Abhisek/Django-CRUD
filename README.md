# Django Project Setup Guide

This guide will help you set up and run the Django project in a virtual environment.

---

## 🐍 1. Set up a Virtual Environment

### 🔹 For Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

### 🔹 For macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

> ✅ Tip: Ensure `python` or `python3` points to Python 3.6+.

---

## 📦 2. Install Dependencies

Once your virtual environment is activated, install all required packages using:

```bash
pip install -r requirements.txt
```

If `requirements.txt` is missing or outdated, you can generate one with:
```bash
pip freeze > requirements.txt
```

---

## 🚀 3. Run the Django Project

### 🔹 Apply Migrations
```bash
python manage.py migrate
```

### 🔹 Start the Development Server
```bash
python manage.py runserver
```

Now visit `http://127.0.0.1:8000/` in your browser to access the project.

---

## 🧪 Optional: Create a Superuser (Admin Access)
```bash
python manage.py createsuperuser
```

Follow the prompts to set up username and password.

---

## 📁 Project Structure Example

```
movies_backend/
└───__pycache__
├───book_store
│   ├───api
│   │   └───__pycache__
│   ├───migrations
│   │   └───__pycache__
│   └───__pycache__
├───movies_backend
│   
└───watchlist_app
    ├───api
    │   └───__pycache__
    ├───migrations
    │   └───__pycache__
    └───__pycache__
```

---

## 🧹 Deactivate Virtual Environment

When you're done, deactivate the virtual environment with:

```bash
deactivate
```

---

## ✅ You're all set!

Happy coding with Django! 🐍🎉
