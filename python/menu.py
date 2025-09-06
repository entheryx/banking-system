#making the main menu for banking-system

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
    
    [3] 	FEEDBACK
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
    [9] 	CHANGE PASSWORD / RESET PIN
    [10] 	TRANSACTIONS (Deposit, Withdraw, Transfer)
    [11]    TRANSACTION HISTROY
    [12]    CLOSE ACCOUNT

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
    [5]     LOAN DEFAULTERS
    [6]     UPDATE ACCOUNT DETAILS
    [7]     DELETE ACCOUNT (Permanent)
    _____________________________________________
    
    [0] 	EXIT
''')
    
    try:
        n = int(input("Choose a menu option: "))
        return n
    except ValueError:
        print("Invalid input, please enter a number.")
        return -1