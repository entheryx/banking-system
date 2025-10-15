import dbConnect as con
import menu
from datetime import date

# ========== BALANCE ENQUIRY ==========

def balance():
    """Gives the current balance in the account"""
    db = con.connect()
    if not db: 
        return
    cu = db.cursor()
    try:
        acct_no = int(input("Enter the account number: "))
        query = "SELECT acct_no, holder_name, initial_balance FROM accHolder WHERE acct_no = %s"
        cu.execute(query, (acct_no,))
        data = cu.fetchone()
        if data:
            print("\n*************** BALANCE ENQUIRY ***************")
            print("Account number: ", data[0])
            print("Name of account holder: ", data[1])
            print("Balance: ", data[2])
            print("*********************************************\n")
        else:
            print("Account not found.")
    except ValueError:
        print("Invalid input. Please enter a numeric account number.")
    except con.Error as err:
        print(f"Database error: {err}")
    finally:
        db.close()


# ========== USER MENU FUNCTIONS ==========

# [6] TRANSACTIONS (Deposit, Withdraw, Transfer)
def user_transactions():
    acct_no = int(input("Enter your account number: "))

    print("\n===== TRANSACTIONS =====")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Transfer")
    choice = int(input("Enter choice: "))

    if choice == 1:  # Deposit
        amt = float(input("Enter amount to deposit: "))
        add_transaction(acct_no, "DEPOSIT", amt)
        update_balance(acct_no, amt, "DEPOSIT")

    elif choice == 2:  # Withdraw
        amt = float(input("Enter amount to withdraw: "))
        if check_balance(acct_no) >= amt:
            add_transaction(acct_no, "WITHDRAW", amt)
            update_balance(acct_no, amt, "WITHDRAW")
        else:
            print("Insufficient Balance!")

    elif choice == 3:  # Transfer
        to_acct = int(input("Enter recipient account no: "))
        amt = float(input("Enter amount to transfer: "))
        if check_balance(acct_no) >= amt:
            add_transaction(acct_no, "TRANSFER_OUT", amt)
            update_balance(acct_no, amt, "WITHDRAW")
            add_transaction(to_acct, "TRANSFER_IN", amt)
            update_balance(to_acct, amt, "DEPOSIT")
            print(f"Transferred {amt} from {acct_no} to {to_acct}")
        else:
            print("Insufficient Balance!")
    else:
        print("Invalid Choice!")


# [7] TRANSACTION HISTORY
def user_transaction_history():
    acct_no = int(input("Enter your account number: "))
    get_transactions_by_account(acct_no)


# ========== ADMIN MENU FUNCTIONS ==========

# [3] VIEW ALL TRANSACTIONS (Daily / Monthly Reports)
def admin_view_transactions():
    print("\n===== TRANSACTION REPORTS =====")
    print("1. Daily Report")
    print("2. Monthly Report")
    print("3. Full Report")
    choice = int(input("Enter choice: "))

    db = con.connect()
    if db is None:
        return
    cursor = db.cursor()

    if choice == 1:
        today = date.today()
        query = "SELECT * FROM transaction WHERE transaction_date = %s"
        cursor.execute(query, (today,))
        print(f"\n Daily Report for {today}:")
    elif choice == 2:
        month = int(input("Enter month (1-12): "))
        year = int(input("Enter year (YYYY): "))
        query = """SELECT * FROM transaction 
                   WHERE MONTH(transaction_date) = %s AND YEAR(transaction_date) = %s"""
        cursor.execute(query, (month, year))
        print(f"\n Monthly Report for {month}/{year}:")
    else:
        query = "SELECT * FROM transaction ORDER BY transaction_date DESC"
        cursor.execute(query)
        print("\n Full Report:")

    records = cursor.fetchall()
    for row in records:
        print(f"ID: {row[0]}, Acc: {row[1]}, Type: {row[2]}, Amt: {row[3]}, Date: {row[4]}")

    cursor.close()
    db.close()


# ========== HELPER FUNCTIONS (all take input inside) ==========

def add_transaction(acct_no=None, transaction_type=None, amount=None):
    if acct_no is None:
        acct_no = int(input("Enter account number: "))
    if transaction_type is None:
        transaction_type = input("Enter transaction type: ").upper()
    if amount is None:
        amount = float(input("Enter amount: "))

    db = con.connect()
    if db is None:
        return
    cursor = db.cursor()

    query = """
        INSERT INTO transactions (acct_no, transaction_type, amount, transaction_date)
        VALUES (%s, %s, %s, %s)
    """
    values = (acct_no, transaction_type, amount, date.today())

    cursor.execute(query, values)
    db.commit()
    cursor.close()
    db.close()


def get_transactions_by_account(acct_no=None):
    if acct_no is None:
        acct_no = int(input("Enter account number: "))

    db = con.connect()
    if db is None:
        return
    cursor = db.cursor()

    query = "SELECT * FROM transactions WHERE acct_no = %s ORDER BY transaction_date DESC"
    cursor.execute(query, (acct_no,))
    records = cursor.fetchall()

    print(f"\n Transactions for Account {acct_no}:")
    for row in records:
        print(f"ID: {row[0]}, Type: {row[2]}, Amount: {row[3]}, Date: {row[4]}")

    cursor.close()
    db.close()


def check_balance(acct_no=None):
    if acct_no is None:
        acct_no = int(input("Enter account number: "))

    db = con.connect()
    if db is None:
        return 0
    cursor = db.cursor()

    query = "SELECT initial_balance FROM accHolder WHERE acct_no = %s"  # FIXED
    cursor.execute(query, (acct_no,))
    result = cursor.fetchone()
    cursor.close()
    db.close()

    return result[0] if result else 0


def update_balance(acct_no=None, amount=None, transaction_type=None):
    if acct_no is None:
        acct_no = int(input("Enter account number: "))
    if amount is None:
        amount = float(input("Enter amount: "))
    if transaction_type is None:
        transaction_type = input("Enter type (DEPOSIT/WITHDRAW/TRANSFER_IN/TRANSFER_OUT): ").upper()

    db = con.connect()
    if db is None:
        return
    cursor = db.cursor()

    if transaction_type in ("DEPOSIT", "TRANSFER_IN"):
        query = "UPDATE accHolder SET initial_balance = initial_balance + %s WHERE acct_no = %s"
    else:  # WITHDRAW, TRANSFER_OUT
        query = "UPDATE accHolder SET initial_balance = initial_balance - %s WHERE acct_no = %s"

    cursor.execute(query, (amount, acct_no))
    db.commit()
    cursor.close()
    db.close()
