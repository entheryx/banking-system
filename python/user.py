import dbConnect as con
import menu

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

def viewLoanStatus():
    """Views the loan status for a specific user."""
    db = con.connect()
    if not db: return
    cu = db.cursor()
    try:
        number = int(input("Enter your account number: "))
        query = "SELECT * FROM loan_acct WHERE acct_no = {}".format(number)
        cu.execute(query)
        data = cu.fetchone()
        if data:
            print("\n*************** LOAN STATUS ***************")
            print("Account Number:", data[0])
            print("Account Holder Name:", data[1])
            print("Loan Taken:", data[2])
            print("Type of Loan:", data[3])
            print("Status of Loan:", data[4])
            print("Months with Interest Unpaid:", data[5])
            print("*******************************************\n")
        else:
            print("No loan information found for this account.")
    except ValueError:
        print("Invalid input for account number.")
    except con.Error as err:
        print(f"Database error: {err}")
    finally:
        db.close()
