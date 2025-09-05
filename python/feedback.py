import dbConnect as con
import menu

db=con.connect()

def new():
    """Allows a user to give feedback."""

    if not db: return
    cu = db.cursor()
    try:
        number = int(input("Enter your account number: "))
        feed = input("Enter your feedback: ")
        query = "INSERT INTO feedback (acct_no, feedback_text) VALUES ({}, '{}')".format(number, feed)
        cu.execute(query)
        db.commit()
        print("Thank you for your feedback!")
    except ValueError:
        print("Invalid input for account number.")
    except con.Error as err:
        print(f"Database error: {err}")
    finally:
        db.close()
    