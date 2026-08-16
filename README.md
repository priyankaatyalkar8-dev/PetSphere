# PetSphere
A Django-based pet care and pet products platform with product management, pet grooming services, shopping cart, orders, bookings.

# 🐾PetSphere

PetSphere is a Django-based web application designed to provide pet owners with a convenient platform for exploring pet products and accessing pet care services from a single place.

The platform combines **pet product shopping** with **pet care services** such as grooming, boarding, training, and treatment information.

## 📌 About the Project

PetSphere is developed using the Django framework and provides separate experiences for **users and administrators**.

Users can browse products and services, add products to their cart, proceed through checkout, place orders, and explore or book pet care services.

Administrators can securely manage products, services, users, orders, bookings, reviews, and other website content through the backend administration panel.

---

## ✨ Features

### 👤 User Features

- 🔐 User Registration & Login
- 🐾 Browse Pet Products
- 🔎 View Product Details
- 🖼️ Product Images
- 🛒 Add Products to Cart
- ➕ Update Cart Quantity
- 🗑️ Remove Products from Cart
- 💳 Checkout
- 📦 Order Management
- ⭐ Product Reviews & Feedback
- 📋 Browse Pet Care Services
- 📅 Service Booking

### 🐶 Pet Care Services

- ✂️ Pet Grooming
- 🏠 Pet Boarding
- 🎓 Pet Training
- 🏥 Pet Treatment Information

### 🔐 Admin Features

- 🔑 Secure Admin Authentication
- 📦 Product Management
- 🖼️ Product Image Management
- 🐶 Service Management
- 👥 User Management
- 🛒 Order Management
- 📅 Booking Management
- ⭐ Review & Feedback Management
- 📝 Website Content Management

---

## 🛠️ Technologies Used

### Frontend

- HTML5
- CSS3
- JavaScript
- Bootstrap

### Backend

- Python
- Django

### Database

- SQLite

### Additional Technologies

- Django Admin
- Django CKEditor
- Pillow

---

## 📂 Project Structure

```text
PetSphere/
│
├── pet/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── petapp/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│   └── ...
│
├── static/
│
├── media/
│   └── uploaded images
│
├── manage.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── fix_booking_reference.py
├── fix_booking_table.py
└── fix_db.py
