# 🚀 MultiMart E-Commerce Backend

<div align="center">

### 🔥 Django REST Framework | JWT Authentication | Razorpay Integration | REST APIs

A scalable and production-ready E-Commerce Backend built with **Django** and **Django REST Framework**, providing secure authentication, product management, order processing, and payment integration.

![Python](https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge\&logo=python)
![Django](https://img.shields.io/badge/Django-REST%20Framework-green?style=for-the-badge\&logo=django)
![SQLite](https://img.shields.io/badge/Database-SQLite-blue?style=for-the-badge\&logo=sqlite)
![JWT](https://img.shields.io/badge/Auth-JWT-orange?style=for-the-badge)
![Razorpay](https://img.shields.io/badge/Payment-Razorpay-success?style=for-the-badge)

</div>

---

# ✨ Features

## 🔐 Authentication & Authorization

* User Registration
* User Login
* User Logout
* JWT Authentication
* Protected API Routes
* User Profile Management

---

## 🛍️ Product Management

* Product Listing API
* Product Detail API
* Category Management
* Product Search
* Product Filtering
* Inventory Management

---

## 🛒 Cart & Order Management

* Add Products to Cart
* Update Cart Quantity
* Remove Cart Items
* Order Creation
* Order Tracking
* Order History

---

## 💳 Payment Integration

* Razorpay Order Creation
* Payment Verification
* Secure Checkout Workflow
* Transaction Validation
* Order Confirmation

---

## ⚡ REST APIs

### Authentication APIs

```http
POST /api/auth/register/
POST /api/auth/login/
POST /api/auth/logout/
GET  /api/auth/profile/
```

### Payment APIs

```http
POST /api/payment/create-order/
POST /api/payment/verify/
```

### Product APIs

```http
GET    /api/products/
GET    /api/products/<id>/
POST   /api/products/
PUT    /api/products/<id>/
DELETE /api/products/<id>/
```

---

# 🏗️ Tech Stack

| Technology            | Purpose              |
| --------------------- | -------------------- |
| Python                | Backend Language     |
| Django                | Web Framework        |
| Django REST Framework | REST APIs            |
| SQLite                | Database             |
| JWT                   | Authentication       |
| Razorpay              | Payment Gateway      |
| CORS Headers          | Frontend Integration |

---

# 📂 Project Structure

```bash
backend
│
├── accounts
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   └── urls.py
│
├── orders
│
├── payments
│
├── store
│
├── ecommerce
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── manage.py
├── requirements.txt
└── db.sqlite3
```

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/narayana-yanamadala/ecommerce-backend.git
```

## Navigate to Project

```bash
cd ecommerce-backend
```

## Create Virtual Environment

```bash
python -m venv venv
```

## Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Apply Migrations

```bash
python manage.py makemigrations

python manage.py migrate
```

---

## Run Development Server

```bash
python manage.py runserver
```

Backend Server:

```bash
http://127.0.0.1:8000
```

---

# 🌐 API Testing

### Register User

```http
POST /api/auth/register/
```

### Login User

```http
POST /api/auth/login/
```

### Get User Profile

```http
GET /api/auth/profile/
```

### Create Payment Order

```http
POST /api/payment/create-order/
```

### Verify Payment

```http
POST /api/payment/verify/
```

---

# 🔒 Security Features

✅ JWT Authentication

✅ Password Hashing

✅ Protected Endpoints

✅ Secure Payment Verification

✅ CSRF Protection

✅ Input Validation

---

# 🚀 Future Enhancements

* Wishlist Functionality
* Product Reviews & Ratings
* Coupon System
* Email Notifications
* Order Tracking
* Admin Dashboard
* PostgreSQL Integration
* Docker Deployment

---

# 👨‍💻 Developer

## Narayana Yanamadala

### Python Full Stack Developer

**Skills**

* Python
* Django
* Django REST Framework
* React.js
* JavaScript
* REST APIs
* Razorpay Integration

### GitHub

https://github.com/narayana-yanamadala/ecommerce-backend.git

---

# ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.

---

<div align="center">

### 🚀 Built with Django & DRF

</div>
