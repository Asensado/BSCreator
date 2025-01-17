#Gabriel Buena
#Computer Science 110
#Final Project
#08/01/2024

#Purpose: Create a Balance Sheet Program

#Pseudocode
'''
    START

    # Import necessary libraries
    IMPORT libraries (csv, os, datetime, pickle, glob, time, signal, sys, configparser)

    # Function: Prevent program exit with Control + C
    DEFINE keyboard_interrupt(signal, frame):
        CALL main_program()

    # Function: Check if business setup exists
    DEFINE check_dependencies():
        IF "config.ini" does not exist:
            CREATE config file with default settings
        ELSE:
            READ config file
            IF "is_run" is False:
                CALL change_business_name()
                SET "is_run" to True in config
                ASK user for tutorial and handle response
            SET global variables for directory and business name

    # Function: Change business name
    DEFINE change_business_name():
        ASK user for new business name
        UPDATE config file with new business name

    # Function: Change save directory
    DEFINE change_directory():
        ASK user for new directory
        UPDATE config file with new directory

    # Function: Clear screen
    DEFINE clear_screen():
        USE appropriate command to clear screen based on OS

    # Function: Display main menu
    DEFINE main_menu():
        LOOP until valid input is received:
            PRINT menu options
            TRY to get user input
            HANDLE invalid inputs
        MATCHCASE user input:
            CASE 1: CALL new_sheet()
            CASE 2: CALL view_saved()
            CASE 3: CALL tutorial()
            CASE 4: CALL settings_menu()
            CASE 5: EXIT program

    # Function: Settings menu
    DEFINE settings_menu():
        LOOP until valid input is received:
            PRINT settings menu
            TRY to get user input
            HANDLE invalid inputs
        MATCHCASE user input:
            CASE 1: CALL change_directory()
            CASE 2: CALL change_business_name()
            CASE 3: RETURN to main menu

    # Function: Get current date
    DEFINE get_date():
        STORE current month and year in global variables

    # Function: Check for existing balance sheet
    DEFINE check_existing_sheet():
        GET date and construct filename
        CHECK if file exists:
            ASK user to overwrite or create new version
        RETURN appropriate filename

    # Function: Create new balance sheet
    DEFINE new_sheet():
        ASK user for numbers of assets, liabilities, equity entities
        ASK user for names and opening balances for each category
        CREATE and WRITE balance sheet CSV
        ASK user for transactions
        UPDATE balance sheet with transaction details
        CALL check_is_balanced() to verify balance
        PRINT success message

    # Function: Check if balance sheet is balanced
    DEFINE check_is_balanced(balance_sheet, assets_count):
        READ last row of balance sheet
        CALCULATE asset and liabilities + equity totals
        IF totals match:
            RETURN "Balanced"
        ELSE:
            RETURN "Not Balanced"

    # Function: View saved balance sheets
    DEFINE view_saved():
        GET all balance sheet files from directory
        PRINT filenames and balance status
        ASK user to return to menu

    # Function: Tutorial
    DEFINE tutorial():
        WALK user through program features step-by-step

    # Main program logic
    DEFINE main_program():
        SET signal handler for keyboard interrupt
        CALL check_dependencies()
        WHILE True:
            CALL main_menu()

    # Start the program
    CALL main_program()

    END
'''

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
import configparser

#Prevents user from exiting the program with Control + C
def keyboard_interrupt(signal, frame):
    program() #Call main program function

#Checks config file
def check_dependencies():
    config = configparser.ConfigParser()
    
    if not path.isfile("config.ini"):
        #Adds sections and contents in config file
        config["General"] = {"business_name": "", "directory": "usr_data", "is_run": False}
        
        with open("config.ini", "w") as config_file:
            config.set("General", "is_run", "True")
            config.write(config_file)
            
        change_business_name()
        
    else:
        config.read("config.ini") #Read config file
        
        config_run = config.getboolean("General", "is_run")
        
        if not config_run:
            change_business_name()
            
            config.set("General", "is_run", "True")
            
            with open("config.ini", "w") as config_file:
                config.write(config_file)
            
            print(f"Is this your first time running this program?\nIf so, would you like to run a tutorial?\n[Y/N]")
            input_question = str(input()).strip().upper()
            match input_question:
                case "Y":
                    tutorial()
                case "N":
                    main_menu()
                case _: #Catch-all that skips the tutorial
                    print(f"Input perceived as \"N\"")
                    pass
            
    config.read("config.ini")
    
    global directory #Create global variable "directory"
    directory = config.get("General", "directory")
    if not path.isdir(directory):
        os.mkdir(directory)
    
    global current_business_name
    current_business_name = config.get("General", "business_name")

def change_business_name():
    clear_screen()
    config = configparser.ConfigParser()
    config.read("config.ini") #Read config file
    
    temp_name = str(input(f"What is the name of the business?\n"))
    global current_business_name
    current_business_name = temp_name
    config.set("General", "business_name", current_business_name)
    
    with open("config.ini", "w") as config_file:
        config.write(config_file)

def change_directory():
    config = configparser.ConfigParser()
    config.read("config.ini")
    
    clear_screen()
    global directory
    directory = str(input("Enter the new directory:\n"))
    
    config.set("General", "directory", directory)
    
    with open("config.ini", "w") as config_file:
        config.write(config_file)
        
    check_dependencies()

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
                print(">> Enter numbers only. Try again.")
                time.sleep(0.3)
            else:
                if input_menu not in range (1, 6): #Checks if input is within 1-5
                    print(f">> Please enter a number from the options.")
                    time.sleep(0.3)
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
            print(">> Enter numbers only. Try again.")
            time.sleep(0.3)
        else:
            if input_menu not in range (1, 4): #Checks if input is within 1-4
                print(">> Please enter a number from the options.")
                time.sleep(0.3)
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
        while True: #Ensures the user enters something
            temp_asset = str(input(f"What is the name of the asset {a + 1}?\n"))
            
            if not len(temp_asset.strip()) == 0:
                lst_assets.append(temp_asset)
                break
            else:
                print(f"Please enter a name.")
                continue
        
    for a in range(amt_liabilities):
        while True: #Ensures the user enters something
            temp_liability = str(input(f"\nWhat is the name of the liability {a + 1}?\n"))
            
            if not len(temp_liability.strip()) == 0:
                lst_liabilities.append(temp_liability)
                break
            else:
                print(f"Please enter a name.")
                continue
    for a in range(amt_equity_entities):
        while True: #Ensures the user enters something
            temp_entity = str(input(f"\nWhat is the name of the equity entity {a + 1}?\n"))
            
            if not len(temp_entity.strip()) == 0:
                lst_equity_entities.append(temp_entity)
                break
            else:
                print(f"Please enter a name.")
                continue
        
    lst_opening_balances = ["Opening Balances"]
    
    while True:
        clear_screen()
        try:
            b = 0
            for a in lst_assets:
                temp_balance = float(input(f"\nWhat is the current opening balance of {a}?\n"))
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
                temp_balance = float(input(f"\nWhat is the current opening balance of {a}?\n"))
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
    print(f"> In the menu, you would start by selecting [1]\n")
    
    time.sleep(2)
    print(f"\n\tMain Menu")
    time.sleep(0.5)
    print(f"\t{current_business_name} Balance Sheet Creator")
    print("==========================================================================")
    print(f"[1]\tCreate or edit a balance sheet")
    print(f"[2]\tView saved balance sheet/s and their status\n")
    input(f"\nPress Enter to continue...")

    time.sleep(0.5)
    print(f"\n{username} entered \"1\"")
    
    time.sleep(2)
    clear_screen()
    print(f">> Next, you would answer the questions asked below.")

    time.sleep(2)
    print(f"How many assets do you have?")
    time.sleep(2)
    print(f"{username} entered \"1\"\n")
    time.sleep(2)
    print(f"How many liabilities do you have?")
    time.sleep(2)
    print(f"{username} entered \"1\"\n")
    time.sleep(2)
    print(f"How many equity entities do you have?")
    time.sleep(2)
    print(f"{username} entered \"1\"\n")
    time.sleep(2)

    lst_assets = ["Bank Account", "Home Bills", username]
    clear_screen()
    
    time.sleep(2)
    print(f"What is the name of the asset 1?")
    time.sleep(2)
    print(f"{username} entered \"Bank Account\"\n")
    
    time.sleep(2)
    print(f"What is the name of the liability 1?")
    time.sleep(2)
    print(f"{username} entered \"Home Bills\"\n")
    time.sleep(2)
    print(f"What is the name of the equity entity 1?")
    time.sleep(2)
    print(f"{username} entered \"{username}\"\n")
        
    lst_opening_balances = ["Opening Balances"]
    
    clear_screen()
    time.sleep(2)
    print(f"What is the current opening balance of your Bank Account?")
    time.sleep(2)
    print(f"{username} entered \"6000\"\n")
    time.sleep(2)
    print(f"What is the current opening balance of your Home Bills?")
    time.sleep(2)
    print(f"{username} entered \"2500\"\n")
    time.sleep(2)
    print(f"What is the current opening balance of your Equity?")
    time.sleep(2)
    print(f"{username} entered \"3500\"\n")
    
    time.sleep(2)
    print(f"\n> At this point, the program saves all your info to a file.")
    print(f"> Now we move onto transactions, which are the dealings a business, or you, do.")
    input("Press Enter to continue...")
    
    clear_screen()
    print(f"How many transactions will you add?")
    time.sleep(1.5)
    print(f"{os.getlogin()} entered \"3\"\n")
    time.sleep(2)
    
    clear_screen()
    print("> For the first two transactions, you're paying your home bills.")
    print("Transaction 1")
    
    print(f"What is the added or subtracted amount of Bank Account?")
    time.sleep(2)
    print(f"{username} entered \"-1000\"\n")
    time.sleep(2)
    print(f"> You put \"-1000\" since you paid $1000 worth of your bills. \n> If you were depositing money, you don't need to add a symbol.")
    time.sleep(3.5)
    print(f"\nWhat is the added or subtracted amount of Home Bills?")
    time.sleep(2)
    print(f"{username} entered \"-1000\"\n")
    time.sleep(2)
    print(f"> You put \"-1000\" since you paid $1000 worth of your bills from your bank account. \n> If you had more bills to pay, you would instead ADD more balance to your bills.")
    time.sleep(0.5)
    
    input("Press Enter to continue...")
    
    print(f"\nTransaction 2")
    time.sleep(2)
    print(f"\nWhat is the added or subtracted amount of Bank Account?")
    time.sleep(2)
    print(f"{username} entered \"-1500\"\n")
    time.sleep(2)
    print(f"What is the added or subtracted amount of Home Bills?")
    time.sleep(2)
    print(f"{username} entered \"-1500\"\n")
    
    input("Press Enter to continue...")
    
    print(f"\n> In this transaction, you received your paycheck of $3000.")
    print(f"\nTransaction 3")
    time.sleep(2)
    print(f"\nWhat is the added or subtracted amount of Bank Account?")
    time.sleep(2)
    print(f"{username} entered \"3000\"\n")
    time.sleep(2)
    print(f"What is the added or subtracted amount of Me?")
    time.sleep(2)
    print(f"{username} entered \"3000\"\n")
    time.sleep(2)
    print(f"> When a business or individual does business (makes money, completes a transaction, etc), their equity also increases because profit adds value to the business.\n")
    print(f"When a company earns more than it spends, the excess gets recorded as earnings, reflecting the owners' claim on the business' assets after the liabilities are paid.\n")
    
    input("Press Enter to create the balance sheet...")
    
    #Creates a new CSV
    current_file = open("tutorial/sample.csv", "w", newline='')
    
    #Combines all asset, liability and equity names into one row
    lst_object_names = ["", "Bank Account", "Home Bills", username]
    lst_categories = ["Transactions", "Assets", "Liabilities", "Equity"]
    lst_opening_balances = ["Opening Balances", 6000, 2500, 3500]
    lst_transaction_1 = ["1", -1000, -1000, 0]
    lst_new_balance_1 = ["New Balance", 5000, 1500, 3500]
    lst_transaction_2 = ["2", -1500, -1500, 0]
    lst_new_balance_2 = ["New Balance", 3500, 0, 3500]
    lst_transaction_3 = ["3", 3000, 0, 3000]
    lst_new_balance_3 = ["New Balance", 6500, 0, 6500]
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

#Callable program loop
def program():
    while True:
        main_menu()


#Start of the program
#Sets Control + C as the signal to listen
signal.signal(signal.SIGINT, keyboard_interrupt)

check_dependencies()
program()
