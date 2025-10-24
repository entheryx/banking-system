# 🏦 Banking System Project

![Python](https://img.shields.io/badge/Python-3.13%2B-blue?logo=python)
![MySQL](https://img.shields.io/badge/MySQL-8.0-orange?logo=mysql)
![License](https://img.shields.io/badge/License-Educational-green)

## 📘 Overview

The **Banking System Project** is a fully functional Python–MySQL application designed for **Class 12 CBSE Computer Science** practicals and real-world learning of backend database systems.  
It simulates essential banking operations such as **account management, transactions, loan processing, and feedback handling**, with separate interfaces for **Admin** and **User**.  

Built using **modular Python scripts** and **MySQL Connector**, this project demonstrates database-driven programming, CRUD operations, and authentication logic in a structured, scalable way.

---

## 🚀 Key Features

### 👨‍💻 User Functionalities
- View account details  
- Update personal information (Name, Email, Phone, Address)  
- Deposit, Withdraw, and Transfer funds  
- Apply for and view loan status  
- Submit feedback  

### 🧑‍💼 Admin Functionalities
- Login authentication for administrators  
- Add, view, and delete account holders  
- Approve or manage loan applications  
- View all transactions and defaulter lists  
- Access and review user feedback  

---

## 🧠 Technologies Used
- **Python 3.13** — Backend programming  
- **MySQL 8.0** — Relational database for persistent data  
- **mysql-connector-python** — For database connectivity  
- **Command Line Interface (CLI)** — For interaction and testing  

---

## 🗃️ Project Structure

```plaintext
banking-system/
├── .gitignore
├── main.py                 # Main entry point of the application
├── README.md               # Project overview and documentation
├── requirements.txt        # Python dependencies
├── python/                 # Core logic of the application
│   ├── admin.py            # Admin-related functionalities
│   ├── dbConnect.py        # MySQL connection handling
│   ├── feedback.py         # Feedback processing functions
│   ├── loan.py             # Loan management logic
│   ├── menu.py             # Interactive command-line menu
│   ├── transactions.py     # Deposit, withdrawal, and transfer logic
│   ├── update.py           # User account info update functions
│   └── user.py             # User-related functionalities
├── sql/                    # Database schema and setup
│   └── schema.sql          # SQL schema setup script
├── .vscode/                # VSCode configuration files
│   └── settings.json
```
---

## 🧱 Database Schema

### Tables:
| Table Name | Description |
|-------------|-------------|
| `accHolder` | Stores account holder details |
| `admin_data` | Contains admin login credentials |
| `transactions` | Stores deposit, withdrawal, and transfer history |
| `Loans` | Stores all loan-related information |
| `feedback` | Stores user feedback and suggestions |

Each table is connected via **foreign key constraints** ensuring relational integrity.

---

## ⚙️ Installation & Setup Guide

### 1️⃣ Prerequisites
- Install **MySQL Server** and **Python 3.13** on your system.  
- Ensure MySQL service is running.  

### 2️⃣ Database Setup
Run the provided SQL script:
```sql
CREATE DATABASE IF NOT EXISTS banking_system;
USE banking_system;

-- Execute contents of schema.sql provided in the project folder
```

### 3️⃣ Install Python Dependencies
```bash
pip install mysql-connector-python
```

### 4️⃣ Configure Database Connection
Edit `dbConnect.py` with your local credentials:
```python
db = con.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="banking_system"
)
```

### 5️⃣ Run the Application
```bash
python menu.py
```

---

## 🧭 Program Flow

```plaintext
User/Admin
   │
   ▼
 menu.py
   ├── userMenu() ───────> users.py, update.py, transactions.py, loan.py, feedback.py
   └── adminMenu() ──────> admin.py, feedback.py, loan.py
                             │
                             ▼
                         dbConnect.py  →  MySQL Database (banking_system)
```

---

## 🧪 Sample Data
- Default admin credentials:  
  **Username:** `admin`  
  **Password:** `password123`
- Preloaded sample users, transactions, and loan records are included in `schema.sql`.

---

## 🌟 Future Enhancements
- Implement GUI using **Tkinter** or **PyQt**  
- Add **user authentication system** with passwords  
- Use **password hashing** for secure admin login  
- Introduce **advanced analytics and reporting dashboard**  
- Enable **email notifications** for transactions and loan approvals  

---

## 🎓 Educational Objective
This project demonstrates:
- Database CRUD operations  
- Menu-driven programming in Python  
- Use of MySQL connector for backend integration  
- Modular programming and function-level abstraction  
- Real-world simulation of a banking management system  

---

## 📞 Contact
For queries, feedback, or contributions:
- GitHub: https://github.com/entheryx
- GitHub: https://github.com/Aurelyx-19

---

## 🪪 License
This project is distributed for **educational and non-commercial use only.**  
Feel free to fork, learn, and improve upon it.

---

### 💬 “Code. Learn. Evolve.”  
> Designed with ❤️ for Coding!

---

🚀 Happy Coding! 🚀
