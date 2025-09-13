#making the main menu for banking-system

import update
#=====================================================
#                   MAIN MENU
#=====================================================

def mainMenu(): #mainmenu
    print('''
    ===========================================================
                    BANK MANAGEMENT SYSTEM
    ===========================================================
''')
    print(''' 
    ------------------MAIN MENU--------------------
    [1]     USER MANAGMENT
    [2]     ADMIN DASHBOARD
    _____________________________________________
    
    [3] 	NEW FEEDBACK
    [4] 	CUSTOMER SUPPORT / HELP DESK ☎️ 
    [0] 	EXIT
''')
    
    try:
        n = int(input("Choose a menu option: "))
        return n
    except ValueError:
        print("Invalid input, please enter a number.")
        return -1


def userMenu():     #usermenu
    print(''' 
    ------------------USER MENU--------------------
    [1] 	ACCOUNT HOLDER DETAILS
    [2] 	VIEW LOAN DETAILS
    [3] 	BALANCE ENQUIRY
    [4] 	UPDATE NAME
    [5] 	UPDATE EMAIL
    [6] 	UPDATE PHONE NUMBER
    [7] 	UPDATE ADDRESS
    [8] 	LOAN SERVICES (Apply / EMI / Check Status)
    [9] 	CLOSE ACCOUNT
    [10] 	TRANSACTIONS (Deposit, Withdraw, Transfer)
    [11]    TRANSACTION HISTROY

    _____________________________________________
    
    [13] 	GIVE FEEDBACK
    [14] 	CUSTOMER SUPPORT / HELP DESK 
    [0] 	EXIT
''')
    
    try:
        n = int(input("Choose a menu option: "))
        return n
    except ValueError:
        print("Invalid input, please enter a number.")
        return -1

def adminMenu():     #adminmenu
    print(''' 
    ------------------ADMIN MENU--------------------
    [1]     VIEW ALL ACCOUNT HOLDERS
    [2]     VIEW FEEDBACK
    [3]     ADD ACCOUNT HOLDER
    [4]     NEW ADMIN ACCOUNT
    [5]     APPROVE LOAN
    [6]     LOAN DEFAULTERS
    [7]     UPDATE ACCOUNT DETAILS
    [8]     DELETE ACCOUNT (Permanent)
    _____________________________________________
    
    [0] 	EXIT
''')
    
    try:
        n = int(input("Choose a menu option: "))
        return n
    except ValueError:
        print("Invalid input, please enter a number.")
        return -1
    
def upgd():
    print(''' 
    ------------------UPDATE MENU--------------------
    [1] 	UPDATE NAME
    [2] 	UPDATE EMAIL
    [3] 	UPDATE PHONE NUMBER
    [4] 	UPDATE ADDRESS
    ''')
    try:
        n = int(input("Choose a menu option: "))
    except ValueError:
        print("Invalid input, please enter a number.")
        
    match n:
        case 1:
            update.name()
        case 2:
            update.email()
        case 3:
            update.phnum()
        case 4:
            update.address() 

