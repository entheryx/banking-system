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
    n=int(input("Choose a menu option using keyboard: "))
    return n


def userMenu():     #usermenu
    print(''' 
    ------------------USER MENU--------------------
	[1] 	ACCOUNT HOLDER DETAILS
	[2] 	UPDATE LOAN STATUS
	[3] 	BALANCE ENQUIRY
	[4] 	UPDATE NAME
	[5] 	UPDATE EMAIL
	[6] 	UPDATE PHONE NUMBER
	[7] 	UPDATE ADDRESS
	[8] 	LOAN SERVICES (Apply / EMI / Check Status)
	[9] 	CHANGE PASSWORD / RESET PIN
	[10] 	CLOSE ACCOUNT

	_____________________________________________
	
	[11] 	GIVE FEEDBACK
	[12] 	CUSTOMER SUPPORT / HELP DESK 
	[0] 	EXIT
''')
    n=int(input("Choose a menu option using keyboard: "))
    return n

def adminMenu():     #adminmenu
    print(''' 
    ------------------ADMIN MENU--------------------
	[1]     VIEW ALL ACCOUNT HOLDERS
	[2]     VIEW FEEDBACK
	[3]     LOAN LENDERS
	[4]     VIEW ALL TRANSACTIONS (Daily / Monthly Reports)
	[5]     LOAN DEFAULTERS
	[6]     UPDATE ACCOUNT DETAILS
        [7]     DELETE ACCOUNT (Permanent)
	_____________________________________________
	
	[0] 	EXIT
''')
    n=int(input("Choose a menu option using keyboard: "))
    return n

