import dbConnect as con
import menu
import mysql.connector

def viewData():
    """Displays account holder's data based on account number."""
    db = con.connect()
    if not db: return
    cu = db.cursor()
    try:
        number = int(input("Enter the account number: "))
        query = "SELECT * FROM accHolder WHERE acct_no = {}".format(number)
        cu.execute(query)
        data = cu.fetchone()  # Fetch one record
        if data:
            print("\n*************** ACCOUNT DETAILS ***************")
            print("Account number: ", data[0])
            print("Name of account holder: ", data[1])
            print("Phone number: ", data[2])
            print("Email: ", data[3])
            print("Address: ", data[4])
            print("Initial balance: ", data[5])
            print("Loan Taken: ", data[6])
            print("*********************************************\n")
        else:
            print("Account not found.")
    except ValueError:
        print("Invalid input. Please enter a numeric account number.")
    except con.Error as err:
        print(f"Database error: {err}")
    finally:
        db.close()

def closeAccount():
    db = con.connect()
    if not db: 
        return
    cu = db.cursor()
    try:
        acct_no = int(input("Enter your account number: "))
        confirm = input("Are you sure you want to close your account? (Y/N): ").strip().lower()
        if confirm != "y":
            print("Account closure cancelled.")
            return

        # Delete all feedback linked to this account
        cu.execute("DELETE FROM feedback WHERE acct_no=%s", (acct_no,))

        cu.execute("DELETE FROM loan_acct WHERE acct_no=%s", (acct_no,))
        cu.execute("DELETE FROM transaction WHERE acct_no=%s", (acct_no,))
        db.commit()


        # Delete from accHolder table
        query = "DELETE FROM accHolder WHERE acct_no = %s"
        cu.execute(query, (acct_no,))
        db.commit()

        if cu.rowcount > 0:
            print(f"Account {acct_no} closed successfully.")
        else:
            print("No account found with that number.")
    except ValueError:
        print("Invalid input. Please enter a numeric account number.")
    except mysql.connector.Error as err:
        print(f"Database error: {err}")
    finally:
        db.close()
