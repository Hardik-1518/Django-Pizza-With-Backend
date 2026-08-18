# Pizzeria TestaResto - Django Pizza E-Commerce Shop

Pizzeria TestaResto is a modern, responsive, and full-featured pizza e-commerce application built with Django. It features a dynamic food catalog, category filtering, a live session-based shopping cart, a secure user login/registration system, an interactive checkout flow, and a client dashboard to track orders.

For the administrators, the project is pre-equipped with the gorgeous, modern **Jazzmin Dashboard** for managing products, categories, orders, and clients seamlessly.

---

## 🍕 Features

* **Dynamic Catalog**: View and search pizzas, beverages, and desserts.
* **Instant Category Filtering**: Filter products by category using outline pill selectors.
* **Live Global Cart**: Dynamic cart update counters and popup previews in the navbar header, updated in real time on every page.
* **Interactive Checkout**: Complete billing details, select payment options (Cash On Delivery or Credit Card), and place orders.
* **Client Dashboard**: Track order history, view detailed order receipts, and print invoices.
* **Modern Interface**: Refactored styling using **Poppins** typography, responsive elements, soft hover transitions, and flat shadows.
* **Jazzmin Admin Panel**: Modern back-end dashboard experience out of the box.
* **Production-Ready Configuration**: Built-in compatibility with **Whitenoise** static files serving and Gunicorn.
* **Persistent DB Support**: Pre-configured dynamic DB pathing to mount persistent volumes on cloud hosts.

---

## 💻 Local Setup and Running

Follow these steps to run the application on your local machine:

### Prerequisite
Ensure you have **Python 3.10+** installed on your system.

### 1. Set Up Virtual Environment
Initialize and activate your virtual environment:
```powershell
# Windows
python -m venv env
env\Scripts\activate

# macOS/Linux
python3 -m venv env
source env/bin/activate
```

### 2. Install Project Dependencies
Install all required modules from `requirements.txt`:
```bash
pip install -r requirements.txt
```

### 3. Apply DB Migrations
Apply Django migrations to prepare the SQLite database:
```bash
python manage.py migrate
```

### 4. Run Development Server
Boot up the local dev server:
```bash
python manage.py runserver
```
Visit the local store in your browser at `http://127.0.0.1:8000/`.

### 5. Accessing Admin Console
Access the Jazzmin admin console at `http://127.0.0.1:8000/admin/`.
* **Username**: `admin`
* **Password**: (Use your configured superuser credentials)

---

## 🚀 Public Hosting on Render (Recommended)

This project contains native Blueprint configurations for deploying to **Render** with a persistent SQLite database (meaning your products and orders won't be wiped out when the service restarts).

### Deploying to Render via Blueprint (One-Click)
1. Commit all your changes and push your project to a new **GitHub** repository.
2. Sign in to your [Render Dashboard](https://render.com/).
3. Click **New** (top right) and select **Blueprint**.
4. Connect your GitHub repository.
5. Render will automatically parse the `render.yaml` configuration in the project root:
   * It mounts a **1 GB persistent disk** at `/data` for your SQLite database.
   * It launches the build pipeline via `./build.sh`.
   * It starts Gunicorn via `gunicorn project.wsgi:application`.
6. Click **Apply** to deploy. Your website will be live in minutes with a secure SSL certificate (`https://`).
