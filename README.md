
# Banking System Project

## 📚 Overview

This **Banking System Project** is a comprehensive Python-based application integrated with MySQL for database management. It is designed as a Class 12 Computer Science project to demonstrate fundamental concepts of backend programming, database handling, and real-world application development.  
The system simulates core functionalities of a banking environment, enabling both **Admin** and **User** operations.

---

## 🏦 Features

### ✅ User Features
- View account details
- Update personal information:
    - Name
    - Email
    - Phone Number
    - Address
- Submit feedback
- View loan status

### ✅ Admin Features
- Add new account holders
- Add new loan accounts for existing users
- Update loan status
- View loan defaulters
- View user feedback
- View detailed loan accounts

---

## ⚙️ Technologies Used

- **Python** – Backend development language
- **MySQL** – Relational database for storing account, loan, feedback, and transaction data
- **mysql-connector-python** – Python library for MySQL connectivity

---

### 💡 Transaction System
- Ensures atomicity and consistency  
- Logs every transaction in the database with timestamps

### 🗄️ Database Integration
- Uses **MySQL** for storing user accounts, transactions, loans, and feedback  
- Enforces strong **foreign key constraints** to maintain data integrity

---
## 📁 Folder Structure

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

## 🧱 Database Structure

### Tables:
1. **acct_holder** – Stores account holder information
2. **admin_data** – Stores admin credentials
3. **loan_acct** – Stores detailed loan information per account
4. **feedback** – Creates & stores user feedback
5. **transaction** – To store transaction functions - withdraw, deposit, history

---

## 🚀 Installation & Setup Guide

### 1️⃣ MySQL Database Setup
- Ensure MySQL server is installed and running.
- Execute the following script to create the database and necessary tables:

```sql
CREATE DATABASE IF NOT EXISTS bank_management_system;
USE bank_management_system;

-- Tables and sample data as provided in the project files
```

### 2️⃣ Python Dependencies
Install required Python library:
```bash
pip install mysql-connector-python
```

### 3️⃣ Configuration
- Modify the database connection function in your Python code:
```python
db = con.connect(
    host="localhost",
    user="root",
    password="your_password",  # Replace with your MySQL password
    database="bank_management_system"
)
```

### 4️⃣ Run the Application
```bash
python main.py
```

---

## 🎯 How to Use

### 👨‍💻 User Flow
1. Run the program.
2. Select **User** from the main menu.
3. Choose desired action:
    - View Account
    - Update Profile Details
    - Provide Feedback
    - Check Loan Status

### 🧑‍💼 Admin Flow
1. Run the program.
2. Select **Admin** from the main menu.
3. Authenticate with username and password (default: `admin` / `password123`).
4. Perform tasks:
    - Add new account or loan data
    - Update loan statuses
    - View defaulters and feedback

---

## 📊 Sample Data Provided
- Default admin credentials: `admin` / `password123`
- Sample users with accounts, loans, and feedback for testing.

---

## ⚡ Future Enhancements
- Implement GUI using frameworks like Tkinter or PyQt
- Enhance security: Use hashed passwords for admin login
- Add transaction history management
- Provide advanced search and reporting features
- Enable user login with passwords

---

## 🎓 Project Purpose

This project serves as a practical demonstration of:
- Database CRUD operations
- User authentication
- Menu-driven console applications
- Separation of admin and user privileges

---

## 📞 Contact

For queries, feedback, or contributions:
- GitHub: https://github.com/entheryx
- GitHub: https://github.com/Aurelyx-19

---

## 📜 License

This project is provided as-is for educational purposes.

---

🚀 Happy Coding! 🚀
