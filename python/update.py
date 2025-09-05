import dbConnect as con
import menu

def name():
    """Updates the name of an account holder."""
    db = con.connect()
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

