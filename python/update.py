import dbConnect as con
import menu

db=con.connect()
def name():
    """Updates the name of an account holder."""
    if not db: return
    cu = db.cursor()
    try:
        number = int(input("Enter the account number: "))
        holder = input("Enter the updated name: ")
        query = "UPDATE accHolder SET holder_name = '{}' WHERE acct_no = {}".format(holder, number)
        cu.execute(query)
        db.commit()
        if cu.rowcount > 0:
            print("Name successfully updated!")
        else:
            print("Account not found or name is the same.")
    except ValueError:
        print("Invalid input for account number.")
    except con.Error as err:
        print(f"Database error: {err}")
    finally:
        db.close()

def email():
    """Updates the email of an account holder."""
    if not db: return
    cu = db.cursor()
    try:
        number = int(input("Enter the account number: "))
        email = input("Enter the updated email: ")
        query = "UPDATE accHolder SET email = '{}' WHERE acct_no = {}".format(email, number)
        cu.execute(query)
        db.commit()
        if cu.rowcount > 0:
            print("Email successfully updated!")
        else:
            print("Account not found or email is the same.")
    except ValueError:
        print("Invalid input for account number.")
    except con.Error as err:
        print(f"Database error: {err}")
    finally:
        db.close()

def phnum():
    """Updates the phone number of an account holder."""
    if not db: return
    cu = db.cursor()
    try:
        number = int(input("Enter the account number: "))
        phone = input("Enter the updated phone number: ")
        query = "UPDATE accHolder SET phone_no = '{}' WHERE acct_no = {}".format(phone, number)
        cu.execute(query)
        db.commit()
        if cu.rowcount > 0:
            print("Phone number successfully updated!")
        else:
            print("Account not found or phone number is the same.")
    except ValueError:
        print("Invalid input for account number.")
    except con.Error as err:
        print(f"Database error: {err}")
    finally:
        db.close()


