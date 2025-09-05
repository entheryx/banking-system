import sys
sys.path.append(r"X:\banking-system\python")

import dbConnect as con
import menu
import user
import update

choice = menu.mainMenu()  # call it once

if choice == 1:
    match menu.userMenu():
        case 1:
            user.viewData()
        case 2:
            pass
        case 3:
            pass
        case 4:
            update.name()

elif choice == 2:
    menu.adminMenu()
else:
    print("Exiting...")
