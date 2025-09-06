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

choice = menu.mainMenu()  # call it once

while (choice==1 or choice==2 or choice==3 or choice==4):
    if choice == 1:
        match menu.userMenu():
            case 1:
                user.viewData()
            case 2:
                user.viewLoanStatus()
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
            case 11:
                feedback.new()
            case _:
                break;
        break; #BREAKING THE WHILE LOOP FOR NOW ---[A]
        
                

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
                    pass
                case 6:
                    pass
                case 7:
                    pass
                case 11:
                    pass
                case _:
                    break;
        else:
            #print("Exiting...")
            pass
        break; #BREAKING THE WHILE LOOP FOR NOW ---[B]
    #choice = menu.mainMenu() --- #BREAKING THE WHILE LOOP FOR NOW ---[C]

'''
NOTE_- REMOVE LINE [A],[B],[C] TO RESTART THE WHILE LOOP
'''    

print("Exited Succesfully!")
print("Thank you for using us")
