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

# Infinite loop for the main menu
while True:
    choice = menu.mainMenu()

    if choice == 1:  # USER MENU
        while True:
            user_choice = menu.userMenu()
            match user_choice:
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
                case 0:
                    break  # go back to main menu
                case _:
                    print("Invalid choice. Try again.")
                    
    elif choice == 2:  # ADMIN MENU
        if admin.auth():
            while True:
                admin_choice = menu.adminMenu()
                match admin_choice:
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
                    case 0:
                        break  # back to main menu
                    case _:
                        print("Invalid choice. Try again.")
        else:
            print("Admin authentication failed.")

    elif choice == 3:
        feedback.new()

    elif choice == 4:
        print('''For further queries:
                  Contact@  -   EMAIL: support@intisvault.bank
                                PHONE: 1800-123-4567 ''')

    elif choice == 0:
        print("Exited Successfully!")
        print("Thank you for using us.")
        break

    else:
        print("Invalid choice, please try again.")
