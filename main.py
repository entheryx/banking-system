import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent / "python"))

import dbConnect as con
import menu
import user
import admin
import update
import feedback
import transactions
import loan


choice = menu.mainMenu()  # call it once


if choice == 1:
    match menu.userMenu():
        case 1:
            user.viewData()
        case 2:
            acct_no = int(input("Enter your account number: "))
            loan.viewLoan(acct_no)
        case 3:
            transactions.balance()
        case 4:
            update.name()
        case 5:
            update.email()
        case 6:
            update.phnum()
        case 7:
            update.address()   
        case 8:
            print("[1] Apply Loan\n[2] View Loan Details\n[3] Check Loan Status")
            try:
                sub = int(input("Enter choice: "))
                acct_no = int(input("Enter your account number: "))
                if sub == 1:
                    amt = float(input("Loan amount: "))
                    tenure = int(input("Tenure (months): "))
                    loan.applyLoan(acct_no, amt, tenure)
                elif sub == 2:
                    loan.viewLoan(acct_no)
                elif sub == 3:
                    loan.checkStatus(acct_no)
                else:
                    print("Invalid loan option.")
            except ValueError:
                print("Invalid input.")
        case 9:
            user.closeAccount()
        case 10:
            transactions.user_transactions()
        case 11:
            transactions.user_transaction_history()
        case 13:
            feedback.new()
        case 14:
            print('''For further queries:
                  Contact@  -   EMAIL: entheryx@gmail.com
                                PHONE: 9903150XXX''')
        case _:
            pass

    
            

elif choice == 2:
    if admin.auth()==True: 
        match menu.adminMenu():
            case 1:
                admin.viewAll()
            case 2:
                feedback.view()
            case 3:
                admin.addData()
            case 4:
                admin.newAdmin()
            case 5:
                admin.approveLoan()
            case 6:
                loan.listDefaulters()
            case 7:
                menu.upgd()
            case 8:
                admin.deleteAccount()
            case _:
                pass
    else:
        #print("Exiting...")
        pass

elif choice ==3:
    feedback.new()

elif choice==4:
    print('''For further queries:
                  Contact@  -   EMAIL: entheryx@gmail.com
                                PHONE: 9903150XXX''')

else:
    pass

print("Exited Succesfully!")
print("Thank you for using us")
