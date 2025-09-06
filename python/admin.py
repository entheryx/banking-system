import dbConnect as con
import menu
import random


def auth(): #when the admin username & password is verified
    """Authenticate admin using username and password."""
    username = input("Enter admin username: ")
    password = input("Enter admin password: ")

    db = con.connect()
    if not db:
        return False
    
    cursor = db.cursor()
    try:
        query = "SELECT * FROM admin_data WHERE username = %s AND password = %s"
        cursor.execute(query, (username, password))
        result = cursor.fetchone()
        
        if result:
            print("\n✅ Admin Login Successful!\n")
            return True
        else:
            print("\n❌ Invalid credentials. Access Denied.\n")
            return False
            
    except con.mysql.connector.Error as err:
        print(f"Database error: {err}")
        return False
    finally:
        db.close()

def addData():
    """Adds a new account holder to the system."""
    db = con.connect()
    if not db: return
    cu = db.cursor()
    try:
        acct_no = random.randint(1000000000, 9999999999)
        name = input("Enter the name of account holder: ")
        phone = input("Enter the phone number: ")
        email = input("Enter the email of account holder: ")
        address = input("Enter the address of account holder: ")
        balance = float(input("Enter the initial balance: "))
        loan_taken = input("Whether loan taken (yes/no): ")
        
        query = "INSERT INTO acct_holder VALUES ({}, '{}', '{}', '{}', '{}', {}, '{}')".format(acct_no, name, phone, email, address, balance, loan_taken)
        cu.execute(query)
        db.commit()
        print(f"Successfully new account was added with A/C No: {acct_no}")
    except ValueError:
        print("Invalid input for balance.")
    except con.Error as err:
        print(f"Database error: {err}")
    finally:
        db.close()

def viewAll():
    """Displays account holder's data based on account number."""
    db = con.connect()
    cu = db.cursor()
    data="54"
    try:
        query = "SELECT * FROM accHolder"
        cu.execute(query)
        while True:
            data = cu.fetchone()  # Fetch one record
            if data is not None:
                print(data)
            else: 
                break
    except con.Error as err:
        print(f"Database error: {err}")
    finally:
        db.close()

def newAdmin():
    """Allows creation of a new admin account."""
    username = input("Enter new admin username: ")
    password = input("Enter new admin password: ")
    
    db = con.connect()
    if not db:
        print("Database connection failed.")
        return

    cu = db.cursor()
    try:
        # Check if username already exists
        cu.execute("SELECT * FROM admin_data WHERE username = %s", (username,))
        if cu.fetchone():
            print("⚠️ Username already exists. Choose a different username.")
            return
        
        # Insert new admin into database
        query = "INSERT INTO admin_data (username, password) VALUES (%s, %s)"
        cu.execute(query, (username, password))
        db.commit()
        
        print(f"\n✅ New admin account created successfully with username: {username}\n")

    except mysql.connector.Error as err:
        print(f"Database error: {err}")
    finally:
        db.close()