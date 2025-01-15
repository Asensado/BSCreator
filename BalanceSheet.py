#Gabriel Buena
#Computer Science 110
#Final Project
#08/01/2024

#Purpose: Create a Balance Sheet Program

#Pseudocode

#End

#Import Python Libraries
import csv
import os
import os.path as path
import datetime
import pickle
import glob
import time
import signal
import sys

#Prevents user from exiting the program with Control + C
def keyboard_interrupt(signal, frame):
    program() #Call main program function

#Check if business name already exists, and create one if not
def check_dependencies():
    #Checks required files
    is_named = path.isfile("business_name.txt")
    is_directed = path.isfile("directory.txt")
    
    try:
        #Asks user to enter a business name if they haven't yet
        if not is_named:
            change_business_name()
        
        #Sets "usr_data" as the default directory if there isn't a directory set
        if not is_directed:
            temp_directory = open("directory.txt", "w")
            temp_directory.write("usr_data")
            global directory
            directory = "usr_data"
            temp_directory.close()
    except PermissionError: #Error occurs when a file is being used by another program, or is not accessible by the user
        print(f"Permission denied: Unable to create required file/s.\nPlease make sure you have the proper permissions.")
    except Exception as e:
        print(f"An error occurred: {e}")
    else:
        with open("business_name.txt", "r") as file_temp: #Opens name file
            global current_business_name #Sets a global variable
            current_business_name = file_temp.read() #Accesses the file containing the business name and sets it as a global variable
        
        with open("directory.txt") as file_temp:
            directory = file_temp.read() #Accesses the file containing the directory and sets it as a global variable
        
        is_path = path.isdir(directory) #Checks if directory exists after a directory path is set
        #Asks the user if they want to run a tutorial
        if not is_path:
            os.mkdir(directory) #Check if user data path exists, and create one if not
            
            print(f"Is this your first time running this program?\nIf so, would you like to run a tutorial?\n[Y/N]")
            input_question = str(input()).upper()
            match input_question:
                case "Y":
                    tutorial()
                case "N":
                    main_menu()
                case _: #Catch-all that skips the tutorial
                    print(f"Input perceived as \"N\"")
                    pass

#Custom clear screen function for cross-platform compatibility
def clear_screen():
    if(os.name == 'posix'): #Posix is identifier for different os'
       os.system('clear')
    else:
       os.system('cls')

def main_menu():
    try:
        while True:
            clear_screen()
            print("==========================================================================")
            print(f"\tMain Menu")
            print(f"\t{current_business_name} Balance Sheet Creator")
            print("==========================================================================")
            print(f"[1]\tCreate or edit a balance sheet")
            print(f"[2]\tView saved balance sheet/s and their status")
            print(f"[3]\tRun the tutorial")
            print(f"[4]\tChange program settings")
            print(f"[5]\tExit Program")
            
            #Error handling for selecting a menu option
            try:
                input_menu = int(input())
            except ValueError: #Lets user know to only enter numbers
                print("\n>> Enter numbers only. Try again.")
                time.sleep(0.5)
            else:
                if input_menu not in range (1, 6): #Checks if input is within 1-5
                    print(f"\n>> Please enter a number from the options.")
                    time.sleep(0.5)
                else:
                    break #Exits loop
    except NameError as error: #This error occurs when the program cannot access business_name.txts due to perms, and does not define current_business_name
        print(f"\n\nAn error has occured. You may not have the appropriate permissions to run this program.\nContact your Administrator for help.\n\nError: {error}")
        input(f"\nPress Enter to exit...")
        sys.exit()
        
    
    #Using match case instead of if statements for cleaner code
    try:
        match input_menu:
            case 1:
                new_sheet()
            case 2:
                view_saved()
            case 3:
                tutorial()
            case 4:
                settings_menu()
            case 5:
                sys.exit() #Built-in exit function, pretty cool
    except UnboundLocalError as error: #Match case would not be able to take input_menu because of the NameError... error
        print(f"\n\nAn error has occured. You may not have the appropriate permissions to run this program.\nContact your Administrator for help.\n\nError: {error}")
        input(f"\nPress Enter to exit...")
        sys.exit()

def settings_menu():
    
    while True:
        clear_screen()
        print(f"\tSettings")
        print("==========================================================================")
        print(f"[1]\tChange default save directory")
        print(f"[2]\tChange business name")
        print(f"[3]\tBack to Main Menu")
        
        try:
            input_menu = int(input())
        except ValueError: #Lets user know to only enter numbers
            print(f"\n>> Enter numbers only. Try again.")
            time.sleep(1)
        else:
            if input_menu not in range (1, 4): #Checks if input is within 1-4
                print(f"\n>> Please enter a number from the options.")
            else:
                break #Exits loop 
    match input_menu:
        case 1:
            change_directory()
        case 2:
            change_business_name()
        case 3:
            program()
 
def get_date():
    global month
    month = datetime.datetime.now().strftime("%B")
    global year
    year = datetime.datetime.now().strftime("%Y")

def check_existing_sheet():
    clear_screen()
    '''
    get_date()
    filename = "usr_data/" + month + "_" + str(year) + "_balance_sheet.csv"
    if path.isfile(filename) == True:
        print(f"A sheet for {month} already exists, overwrite?\n[Y/N] ")
        temp_input = str(input(""))
        if temp_input.upper() == "Y":
            return
        else:
            main_menu()
    else:
        return
    
    
    get_date()
    filename = "usr_data/" + month + "_" + str(year) + "_balance_sheet.csv"
    x = 1
    if path.isfile(filename) == True:
      unique_filename = "usr_data/" + month + "_" + str(year) + "_" + str(x) + "_balance_sheet.csv"
      while path.isfile(unique_filename) == True:
          x += 1
          unique_filename = "usr_data/" + month + "_" + str(year) + "_" + str(x) + "_balance_sheet.csv"
      return unique_filename
    else:
        return filename
    '''
    
    get_date()
    filename = directory + "/" + month + "_" + str(year) + "_balance_sheet.csv"
    x = 1
    if path.isfile(filename) == True:
        print(f"A sheet for {month} already exists, overwrite?\n[Y/N] ")
        temp_input = str(input(""))
        if temp_input.upper() == "Y":
            return filename
        else:
            unique_filename = directory + "/" + month + "_" + str(year) + "_" + "_balance_sheet_" + str(x) +".csv"
            while path.isfile(unique_filename) == True:
                x += 1
                unique_filename = directory + "/" + month + "_" + str(year) + "_" + "_balance_sheet_" + str(x) +".csv"
            return unique_filename
    else:
        return filename

def change_directory():
    clear_screen()
    directory = str(input("Enter the new directory:\n"))
    
    with open("directory.txt", "w") as file:
        file.write(directory)
        
    check_dependencies()

def change_business_name():
    #Ask and store name of business
    file_name_business = open("business_name.txt", "w")
    name_business = str(input(f"What is the name of the business?\n"))
    global current_business_name
    current_business_name = name_business
    file_name_business.write(name_business)
    file_name_business.close()

def new_sheet():
    clear_screen()
    get_date()
    date = datetime.datetime.now().date()
    #These variables will be used for For loops to store names into lists
    
    print(">> Press Control + C anytime to return to the main menu.")
    time.sleep(2)
    
    while True:
        clear_screen()
        try:
            amt_assets = int(input(f"How many assets do you have?\n"))
            amt_liabilities = int(input(f"How many liabilities do you have?\n"))
            amt_equity_entities = int(input(f"How many equity entities do you have?\n"))
        except ValueError: #Lets user know to only enter numbers
            clear_screen()
            print(">> Enter numbers only. Try again.")
            time.sleep(0.5)
        else:
            break
    
    lst_assets = []
    lst_liabilities = []
    lst_equity_entities = []

    lst_categories = ["Transactions", "Assets"]
    
    lst_empty = [""]
    
    clear_screen()
    
    for a in range(amt_assets):
        temp_asset = str(input(f"What is the name of the asset {a + 1}?\n"))
        lst_assets.append(temp_asset)
        
    for a in range(amt_liabilities):
        temp_liability = str(input(f"What is the name of the liability {a + 1}?\n"))
        lst_liabilities.append(temp_liability)
    for a in range(amt_equity_entities):
        name_current_entity = str(input(f"What is the name of the equity entity {a + 1}?\n"))
        lst_equity_entities.append(name_current_entity)
        
    lst_opening_balances = ["Opening Balances"]
    
    while True:
        clear_screen()
        try:
            b = 0
            for a in lst_assets:
                temp_balance = float(input(f"What is the current opening balance of {a}?\n"))
                lst_opening_balances.append(temp_balance)
                
                if b >= 1:
                    lst_categories.append("")
                b += 1
            
            lst_categories.append("Liabilities")
            b = 0
            for a in lst_liabilities:
                temp_balance = float(input(f"What is the current opening balance of {a}?\n"))
                lst_opening_balances.append(temp_balance)
                
                if b >= 1:
                    lst_categories.append("")
                b += 1

            lst_categories.append("Equity")
            b = 0
            for a in lst_equity_entities:
                temp_balance = float(input(f"What is the current opening balance of {a}?\n"))
                lst_opening_balances.append(temp_balance)
                
                if b >= 1:
                    lst_categories.append("")
                b += 1
        except ValueError:
            clear_screen()
            print("Enter numbers only. Exclude \"$\". Try again.")
            time.sleep(0.5)
        else:
            break
    
    #Creates a new CSV
    filename = check_existing_sheet()
    current_file = open(filename, "w", newline='')
    
    #Combines all asset, liability and equity names into one row
    lst_object_names = lst_assets + lst_liabilities + lst_equity_entities
    
    #Sets created balance sheet as the file to edit
    current_balance_sheet = csv.writer(current_file)
    current_balance_sheet.writerow(lst_categories)
    current_balance_sheet.writerow(lst_empty + lst_object_names)
    current_balance_sheet.writerow(lst_opening_balances)
    
    while True:
        clear_screen()
        try:
            amt_transactions = int(input(f"How many transactions will you add?\n"))
        except ValueError:
            clear_screen()
            print("Enter numbers only. Try again.")
            time.sleep(0.5)
        else:
            break
    
    lst_previous_row = lst_opening_balances
    
    clear_screen()
    for a in range(amt_transactions):
        transaction_balance = []
        transaction_balance.append(a + 1)
        print(f"Transaction {a + 1}")
        for b in lst_assets:
            temp_balance = float(input(f"What is the added or subtracted amount of {b}?\n"))
            transaction_balance.append(temp_balance)
        for b in lst_liabilities:
            temp_balance = float(input(f"What is the added or subtracted amount of {b}?\n"))
            transaction_balance.append(temp_balance)
        for b in lst_equity_entities:
            temp_balance = float(input(f"What is the added or subtracted amount of {b}?\n"))
            transaction_balance.append(temp_balance)
        
        current_balance_sheet.writerow(transaction_balance)
        
        new_balance = [c + d for c, d in zip(lst_previous_row[1:], transaction_balance[1:])]
        new_balance.insert(0, "New Balance")
        
        current_balance_sheet.writerow(new_balance)
        
        lst_previous_row = new_balance
    
    current_file.close()
    is_balanced = check_is_balanced(filename, amt_assets)
    print(f"\n{is_balanced}")
    
    print(f"\nBalance Sheet created successfully for {month} {year}.\nSaved at {filename}\n")
    
    input(f"\nPress Enter to go back to the menu...")

def check_is_balanced(balance_sheet, assets):
    
    stripped_filename = balance_sheet.replace(".csv", "")
    data_filename = stripped_filename + ".bin"
    
    with open(balance_sheet, "r") as file:
        reader = csv.reader(file)
        rows = list(reader)
        
        # Get the last row
        last_row = rows[-1]
        
        # Convert values from index 1 to 'assets' into integers and sum them
        values_to_sum = last_row[1:assets+1]
        asset_sum = sum(map(float, values_to_sum))
        
        values_to_sum = last_row[assets+1:]
        other_sum = sum(map(float, values_to_sum))
        
        if asset_sum == other_sum:
            with open(data_filename, 'wb') as data:
                pickle.dump(True, data)
            return "Sheet is balanced."
        else:
            with open(data_filename, 'wb') as data:
                pickle.dump(False, data)
            return "Sheet is not balanced, please review."

def view_saved():
    clear_screen()
    temp_directory = directory + "/*.csv"
    
    csv_files = glob.glob(temp_directory) #Lol 'glob glob'
    
    temp_directory = directory + "\\"
    
    csv_files = [sheets.replace(temp_directory, "") for sheets in csv_files] #List comprehensions are weird, but extremely useful

    if len(csv_files) < 1:
        print(f"No sheets found under folder {directory}")
        input(f"\nPress Enter to go back to the main menu...")
        return

    temp_directory = directory + "/*.bin"
    data_files = glob.glob(temp_directory)
    
    temp_directory = directory + "\\"
    temp_replace = directory + "/"
    data_files = [bins.replace(temp_directory, temp_replace) for bins in data_files]
    
    b = 0
    for a in csv_files:
        current_bin = "Not yet checked."
        
        if not b >= len(data_files):
            with open(data_files[b], "rb") as bin:
                current_bin = str(pickle.load(bin))
            b += 1
        print(f"\n{a}\tIs Balanced? - {current_bin}")
    print("")
    
    input(f"\nPress Enter to go back to the main menu...")
    return

def tutorial():
    clear_screen()
    get_date()
    username = str(os.getlogin())
    if not path.isdir("tutorial"):
        os.mkdir("tutorial")

    print("================================================================")
    print("Program Tutorial")
    print("Hands-free, no need to press anything unless told so.")
    print(">> Press Control + C anytime to return to the main menu.")
    print(f"===============================================================\n")
    time.sleep(5)
    print(f"> What is a balance sheet?")
    time.sleep(2)
    print(f"A balance sheet is a summary that contains all of an entity's assets and liabilities at a specific point in time.\n")
    time.sleep(3)
    print(f"The balance sheet must always be balanced, as the business has to pay for the things it owns (assets) by borrowing money (liabilities) or from investors (equity).\n")
    time.sleep(4)
    print(f"\nAssets = Liabilities + Equities\nThis is the formula for the balance sheet, calculated by the program.\n")
    
    input(f"\nPress Enter to continue...")
    print(f"__________________________________________________\n")
    time.sleep(0.5)
    
    clear_screen()
    print(f"> How to use the program to create balance sheets?")
    time.sleep(2)
    print(f"We'll create a simple balance sheet for ourselves, to keep track of personal expenses.")
    time.sleep(3)
    print(f"> In the menu, start by selecting [1]\n")
    
    time.sleep(5)
    print(f"\n\tMain Menu")
    time.sleep(0.5)
    print(f"\t{current_business_name} Balance Sheet Manager")
    print("==========================================================================")
    print(f"[1]\tCreate or edit a balance sheet")
    print(f"[2]\tView saved balance sheet/s and their status\n")
    input(f"\nPress Enter to continue...")

    time.sleep(0.5)
    print(f"\n{username} entered \"1\"")
    
    time.sleep(2)
    clear_screen()
    print(f">> Next, answer the questions asked below.")

    time.sleep(2.5)
    print(f"How many assets do you have?")
    time.sleep(2.5)
    print(f"{username} entered \"1\"\n")
    time.sleep(2.5)
    print(f"How many liabilities do you have?")
    time.sleep(2.5)
    print(f"{username} entered \"1\"\n")
    time.sleep(2.5)
    print(f"How many equity entities do you have?")
    time.sleep(3)
    print(f"{username} entered \"1\"\n")
    time.sleep(2.5)

    lst_assets = ["Bank Account", "Home Bills", username]
    clear_screen()
    
    time.sleep(2.5)
    print(f"What is the name of the asset 1?")
    time.sleep(2.5)
    print(f"{username} entered \"Bank Account\"\n")
    
    time.sleep(2.5)
    print(f"What is the name of the liability 1?")
    time.sleep(2.5)
    print(f"{username} entered \"Home Bills\"\n")
    time.sleep(2.5)
    print(f"What is the name of the equity entity 1?")
    time.sleep(2.5)
    print(f"{username} entered \"{username}\"\n")
        
    lst_opening_balances = ["Opening Balances"]
    
    clear_screen()
    time.sleep(2.5)
    print(f"What is the current opening balance of your Bank Account?")
    time.sleep(2.5)
    print(f"{username} entered \"6000\"\n")
    time.sleep(2.5)
    print(f"What is the current opening balance of your Home Bills?")
    time.sleep(2.5)
    print(f"{username} entered \"2500\"\n")
    time.sleep(2.5)
    print(f"What is the current opening balance of your Equity?")
    time.sleep(2.5)
    print(f"{username} entered \"3500\"\n")
    
    time.sleep(3)
    print(f"\n> At this point, the program saves all your info to a file.")
    print(f"> Now we move onto transactions, which are the dealings a business, or you, do.")
    input("Press Enter to continue...")
    
    clear_screen()
    print(f"How many transactions will you add?")
    time.sleep(1.5)
    print(f"{os.getlogin()} entered \"2\"\n")
    time.sleep(2.5)
    print(f"\n> This means you paid for your Home Bills twice in the month.\n")
    time.sleep(3)
    
    clear_screen()
    print("Transaction 1")
    
    print(f"What is the added or subtracted amount of Bank Account?")
    time.sleep(2.5)
    print(f"{username} entered \"-1000\"\n")
    time.sleep(2.5)
    print(f"> You put \"-1000\" since you paid $1000 worth of your bills. \n> If you were depositing money, you would remove \"-\".")
    time.sleep(5)
    print(f"\nWhat is the added or subtracted amount of Home Bills?")
    time.sleep(2.5)
    print(f"{username} entered \"-1000\"\n")
    time.sleep(2.5)
    print(f"> You put \"-1000\" since you paid $1000 worth of your bills from your bank account. \n> If you had more bills to pay, you would remove \"-\".")
    time.sleep(1.5)
    
    input("Press Enter to continue...")
    
    print(f"\nTransaction 2")
    time.sleep(2.5)
    print(f"\nWhat is the added or subtracted amount of Bank Account?")
    time.sleep(2.5)
    print(f"{username} entered \"-1500\"\n")
    time.sleep(2.5)
    print(f"What is the added or subtracted amount of Home Bills?")
    time.sleep(2.5)
    print(f"{username} entered \"-1500\"\n")
    
    input("Press Enter to create the balance sheet...")
    
    #Creates a new CSV
    current_file = open("tutorial/sample.csv", "w", newline='')
    
    #Combines all asset, liability and equity names into one row
    lst_object_names = ["", "Bank Account", "Home Bills", {username}]
    lst_categories = ["Transactions", "Assets", "Liabilities", "Equity"]
    lst_opening_balances = ["Opening Balances", 6000, 2500, 3500]
    lst_transaction_1 = ["1", -1000, -1000, 0]
    lst_new_balance_1 = ["New Balance", 5000, 1500, 3500]
    lst_transaction_2 = ["2", -1500, -1500, 0]
    lst_new_balance_2 = ["New Balance", 3500, 0, 3500]
    lst_empty = []
    
    
    #Sets created balance sheet as the file to edit
    current_balance_sheet = csv.writer(current_file)
    current_balance_sheet.writerow(lst_categories)
    current_balance_sheet.writerow(lst_empty + lst_object_names)
    current_balance_sheet.writerow(lst_opening_balances)
    current_balance_sheet.writerow(lst_transaction_1)
    current_balance_sheet.writerow(lst_new_balance_1)
    current_balance_sheet.writerow(lst_transaction_2)
    current_balance_sheet.writerow(lst_new_balance_2)
    
    
    current_file.close()
    is_balanced = check_is_balanced("tutorial/sample.csv", 1)
    print("Loading...")
    time.sleep(5)
    print(f"\n{is_balanced}")
    time.sleep(3)
    print(f"\nBalance Sheet created successfully for {month} {year}.\nSaved at tutorial/sample.csv\n")
    
    time.sleep(3)
    input("Press Enter to view the balance sheet created for you...")
    os.system("start excel tutorial/sample.csv")
    
    time.sleep(5)
    input(f"\nPress Enter to go back to the main menu...")

def program():
    while True:
        main_menu()

#Sets Control + C as the signal to listen
signal.signal(signal.SIGINT, keyboard_interrupt)

check_dependencies()
program()