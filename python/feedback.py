import dbConnect as con
import mysql.connector
import menu
from mysql.connector import Error


def new():
    """Allows a user to give feedback."""

    db=con.connect()
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
    except mysql.connector.Error as err:
        print(f"Database error: Account Number may not exist!!")
    finally:
        db.close()
    
def view():
    """Displays all user feedback."""
    db=con.connect()
    if not db: return
    cu = db.cursor()
    try:
        query = "SELECT * FROM feedback"
        cu.execute(query)
        data = cu.fetchall()
        if data:
            print("\n*************** USER FEEDBACKS ***************")
            for row in data:
                print(f"Account Number: {row[0]}")
                print(f"Feedback: {row[1]}")
                print("-----------------------------------------")
            print("**********************************************\n")
        else:
            print("No feedback found.")
    except con.Error as err:
        print(f"Database error: {err}")
    finally:
        db.close()

