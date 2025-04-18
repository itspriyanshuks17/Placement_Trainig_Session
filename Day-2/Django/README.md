# 🛍️ Flipkart Django Project

A Django-based e-commerce web application for showcasing and selling electronic items. This project simulates a mini Flipkart-like platform, designed using Django's MVC (Model-View-Controller) architecture.

---

## 📌 Table of Contents

- [About the Project](#about-the-project)  
- [Features](#features)  
- [Project Structure](#project-structure)  
- [Setup and Installation](#setup-and-installation)  
  - [Prerequisites](#prerequisites)  
  - [Virtual Environment Setup](#virtual-environment-setup)  
  - [Installing Dependencies](#installing-dependencies)  
- [Creating the Project & App](#creating-the-project--app)  
- [Django Project Configuration](#django-project-configuration)  
- [Running the Server](#running-the-server)  
- [Admin Panel](#admin-panel)  
- [Database Setup](#database-setup)  
- [Request Flow in Django](#request-flow-in-django)  
- [Contributing](#contributing)  
- [License](#license)

---

## 🛒 About the Project

This is a simple Django e-commerce web app focused on electronics. It allows an admin to manage products and users to browse them. The admin interface is built-in using Django's admin site.

---

## ✨ Features

- Django admin dashboard  
- Product listing and image upload  
- Clean URL routing  
- Templates for dynamic HTML rendering  
- Modular code structure  

---

## 📁 Project Structure

```
flipkart/
├── flipkart/               # Project config
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── electronics/            # Main app for handling electronics
│   ├── admin.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── templates/
│       └── electronics/
│           └── index.html
│
├── static/                 # CSS/JS files
├── manage.py
└── venv/                   # Virtual Environment (optional)
```

---

## 🧰 Setup and Installation

### ✅ Prerequisites

- Python 3.x  
- pip (Python package manager)  
- Optional: `virtualenv` for isolated environments

---

### 🔄 Virtual Environment Setup

**Create a virtual environment:**

```bash
python -m venv venv
```

**Activate the environment:**

- **Windows:**
  ```bash
  venv\Scripts\activate
  ```
- **Linux/Mac:**
  ```bash
  source venv/bin/activate
  ```

---

### 📦 Installing Dependencies

**Install Django:**

```bash
pip install django
```

**Install Pillow (for image handling):**

```bash
pip install pillow
```

---

## ⚙️ Creating the Project & App

**Start a new Django project:**

```bash
django-admin startproject flipkart
cd flipkart
```

**Create the electronics app:**

```bash
python manage.py startapp electronics
```

---

## 🧩 Django Project Configuration

### 1. Add app to `INSTALLED_APPS`

Edit `flipkart/settings.py`:

```python
INSTALLED_APPS = [
    ...
    'electronics',
]
```

### 2. Set up URL Routing

#### `flipkart/urls.py`

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('electronics.urls')),
]
```

#### `electronics/urls.py`

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
```

### 3. Create a view

#### `electronics/views.py`

```python
from django.shortcuts import render

def index(request):
    return render(request, 'electronics/index.html')
```

### 4. Create a template

**File path:**
```
electronics/templates/electronics/index.html
```

**Example HTML:**

```html
<h1>Welcome to the Flipkart Electronics Store</h1>
```

---

## 🚀 Running the Server

Start the development server:

```bash
python manage.py runserver
```

**Visit:** [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## 🛠️ Database Setup

### 1. Create model migrations

```bash
python manage.py makemigrations
```

This creates a file with an ID column and model fields.

### 2. Apply migrations

```bash
python manage.py migrate
```

This applies changes to your actual database.

---

## 🔐 Admin Panel

### 1. Create a superuser

```bash
python manage.py createsuperuser
```

Follow the prompts to set username, email, and password.

### 2. Register models

Edit `electronics/admin.py`:

```python
from django.contrib import admin
from .models import YourModel

admin.site.register(YourModel)
```

### 3. Access the admin dashboard

**URL:** [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

---

## 🔄 Request Flow in Django

```
User sends GET request to 127.0.0.1:8000/
       ↓
Project URLs (flipkart/urls.py)
       ↓
App URLs (electronics/urls.py)
       ↓
View Function (electronics/views.py)
       ↓
Template Rendering (electronics/templates/electronics/index.html)
       ↓
Response sent back to browser
```

Visual summary:

> **Browser Request** → `Project URLs` → `App URLs` → `views.py` function runs → `HttpResponse` or HTML page rendered

---

## 🤝 Contributing

1. Fork this repo  
2. Create your feature branch (`git checkout -b feature/YourFeature`)  
3. Commit your changes (`git commit -m 'Add your message'`)  
4. Push to the branch (`git push origin feature/YourFeature`)  
5. Open a Pull Request  

---

## 📄 License

This project is not licensed.

