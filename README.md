# Inventory Management System

A robust, modern Inventory Management System built with Django and MySQL. It features role-based access control, a sleek dashboard, product and supplier management, and graphical reporting.

## 🚀 Features

* **Interactive Dashboard:** View all products, stock levels, prices, and visual status indicators (In Stock, Low Stock, Out of Stock).
* **Product Management:** Add, edit, and delete products easily from the dashboard.
* **Supplier Management:** Maintain a directory of suppliers (Name, Contact, Email) linked directly to products.
* **Role-Based Access Control (RBAC):**
  * **Admin (Superuser):** Full access to add, edit, and delete products and suppliers.
  * **Staff:** Can view the dashboard and add new products/suppliers.
  * **User:** Read-only access to view the dashboard and stock levels.
* **Reports & Analytics:** Visual representation of stock using Chart.js, highlighting Total Products, Low Stock items, and Healthy Stock items.
* **Modern UI:** Responsive, clean interface built using Bootstrap 5 and custom CSS.

## 🛠️ Tech Stack

* **Backend:** Python, Django 4.2
* **Database:** MySQL
* **Frontend:** HTML, CSS, Bootstrap 5, JavaScript, Chart.js

## 📋 Prerequisites

Before you begin, ensure you have the following installed on your local machine:
* Python 3.x
* MySQL Server (running on localhost:3306)

## ⚙️ Installation & Setup

Follow these steps to get your development environment running:

**1. Clone the repository:**
```
git clone [https://github.com/sashi921/inventory-management.git](https://github.com/sashi921/inventory-management.git)
cd inventory-management
```
**2. Create and activate a virtual environment (Recommended):**
```
python -m venv venv

# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```
**3. Install Dependencies:**
Install Django and the required MySQL database connector:
```
pip install django mysqlclient
```
**4. Database Configuration:**
Open your MySQL client or command line and create the database expected by the application:
```
CREATE DATABASE inventory;
```
Note: The application settings.py is configured to use the MySQL root user with no password on localhost. If your local MySQL setup requires a password, update the DATABASES dictionary inside inventory_project/settings.py.
