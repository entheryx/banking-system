import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent / "python"))

import dbConnect as con
import menu
import user
import update
import feedback
import transactions

choice = menu.mainMenu()  # call it once

if choice == 1:
    match menu.userMenu():
        case 1:
            user.viewData()
        case 2:
            pass
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
             

elif choice == 2:
    menu.adminMenu()
else:
    print("Exiting...")
