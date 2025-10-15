import dbConnect as con

def applyLoan(acct_no, loan_amount, tenure_months):
    """Apply for a new loan"""
    db = con.connect()
    if not db: return
    cu = db.cursor()

    
    rate = 0.075 / 12   # monthly 7.5% annual interest
    n = tenure_months
    P = loan_amount
    emi = (P*rate*(1+rate)**n) / ((1+rate)**n - 1)

    query = "INSERT INTO Loans (acct_no, loan_amount, tenure_months, emi_amount) VALUES (%s,%s,%s,%s)"
    cu.execute(query, (acct_no, loan_amount, tenure_months, round(emi,2)))
    db.commit()
    print(f"Loan request submitted. EMI = {emi:.2f}")
    db.close()

def viewLoan(acct_no=None):
    """View all loans for a user"""
    if acct_no is None:
        try:
            acct_no = int(input("Enter account number: "))
        except ValueError:
            print("Invalid input. Please enter a numeric account number.")
            return
    db = con.connect()
    if not db: return
    cu = db.cursor()
    try:
        cu.execute("SELECT loan_id, acct_no, loan_amount, interest_rate, tenure_months, emi_amount, status, issued_date FROM Loans WHERE acct_no = %s", (acct_no,))
        loans = cu.fetchall()
        if loans:
            print("\n*************** LOAN DETAILS ***************")
            for loan in loans:
                print(f"Loan ID: {loan[0]}")
                print(f"Account Number: {loan[1]}")
                print(f"Loan Amount: {float(loan[2]):.2f}")
                print(f"Interest Rate: 7.50%")  # Fixed rate as per applyLoan()
                print(f"Tenure (Months): {loan[3]}")
                print(f"EMI Amount: {float(loan[4]):.2f}")
                print(f"Status: {loan[5]}")
                print(f"Application Date: {loan[6]}")
                print("-----------------------------------------")
            print("********************************************\n")
        else:
            print("No loans found for this account.")
    except con.errors.Error as err:
        print(f"Database error: {err}")
    finally:
        cu.close()
        db.close()

def checkStatus(acct_no):
    """Check loan status"""
    db = con.connect()
    cu = db.cursor()
    cu.execute("SELECT loan_id, status FROM Loans WHERE acct_no = %s", (acct_no,))
    for l in cu.fetchall():
        print(f"Loan {l[0]}: {l[1]}")
    db.close()

def listDefaulters():
    """Admin: view loan defaulters"""
    db = con.connect()
    cu = db.cursor()
    cu.execute("""SELECT l.loan_id, a.holder_name, l.loan_amount, l.status
                  FROM Loans l
                  JOIN accHolder a ON l.acct_no=a.acct_no
                  WHERE l.status='DEFAULT'""")
    for row in cu.fetchall():
        print(row)
    db.close()
