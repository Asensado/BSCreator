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