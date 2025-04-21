# 🛠️ Django Project Setup & Workflow Guide

This README serves as a step-by-step guide to set up and run a Django project, using an example project named `flipkart` and an app called `Electronics`.

---

## 🐍 Virtual Environment Setup

### 1. Create a Virtual Environment
```bash
python -m venv venv
```
This command sets up a virtual environment named `venv` in your current directory. It helps isolate dependencies for your project.

### 2. Activate the Virtual Environment

#### On Windows:
```bash
venv\Scripts\activate
```

#### On Linux/Mac:
```bash
source venv/bin/activate
```

---

## 📦 Install Django

```bash
pip install django
```
This installs Django in your virtual environment.

---

## 🚀 Start a New Django Project

```bash
django-admin startproject flipkart
cd flipkart
```
- `startproject` initializes a new Django project called `flipkart`.
- `cd flipkart` moves into the project directory.

---

## 🧱 Create a New App

```bash
python manage.py startapp Electronics
```
This creates a new Django app named `Electronics` inside the project.

---

## 🛠️ Register the App in `settings.py`

Open `flipkart/settings.py`, and add `'Electronics'` to the `INSTALLED_APPS` list:
```python
INSTALLED_APPS = [
    ...
    'Electronics',
]
```

---

## ▶️ Run the Development Server

```bash
python manage.py runserver
```
Starts the local development server at `http://127.0.0.1:8000/`.

---

## 🌐 Routing Flow

1. User makes a request in the browser.
2. **Project-level `urls.py`** routes the request to the **app-level `urls.py`**.
3. **App `urls.py`** routes to a **view function** in `views.py`.
4. The **view** renders a **template (HTML page)**.

Example:
```
Browser → Project URLs → App URLs → views.py → templates
```

---

## 🧩 Templates Directory Structure

You should organize your templates like this:
```
Electronics/
└── templates/
    └── Electronics/
        └── index.html
```

This allows Django to find the templates based on app name.

---

## 🔧 Django Admin Setup

### Access Admin Panel:
```
http://127.0.0.1:8000/admin/
```

### Create a Superuser:
```bash
python manage.py createsuperuser
```
Follow the prompts to set username, email, and password.

### Register a Model in Admin:
In `Electronics/admin.py`, register your models:
```python
from .models import YourModel
admin.site.register(YourModel)
```

---

## 🗃️ Migrations

### Create Migration Files:
```bash
python manage.py makemigrations
```
Creates migration files from the models you've defined.

### Apply Migrations to Database:
```bash
python manage.py migrate
```
Applies the changes to your SQLite (or other) database.

---

## 🖼️ Install Pillow (Image Support)

```bash
pip install pillow
```
Pillow is a Python Imaging Library used for handling image fields in Django models.

---

## 🔁 Request-Response Cycle Overview

When a request is made to `127.0.0.1:8000`, the following steps occur:
1. **Project `urls.py`** receives the request.
2. The request is passed to the **App `urls.py`**.
3. A **view function** is executed from `views.py`.
4. The **view** returns a `HttpResponse` or renders a **template**.

---

## ✅ Example Summary

To see your app in action:
- Create a model in `models.py`
- Register it in `admin.py`
- Perform `makemigrations` and `migrate`
- Access `127.0.0.1:8000/admin/` to manage data

---
