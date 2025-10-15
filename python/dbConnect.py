import mysql.connector as con

# --- DATABASE CONNECTION FUNCTION ---
def connect():
    """Establishes and returns a database connection."""
    try:
        db = con.connect(
            host="localhost",
            user="root",
            password="mypass", 
            database="banking_system"
        )
        return db
    except con.Error as err:
        print(f"Error connecting to database: {err}")
        print("Please ensure MySQL is running, the database 'bank_management_system' exists, and the credentials are correct.")
        return None