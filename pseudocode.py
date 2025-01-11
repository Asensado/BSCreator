'''
START Program
  DEFINE Purpose: Create a Balance Sheet Program

  DEFINE Variables
    - Amounts: amt_name
    - Names: name_name
    - Lists: lst_name
    - Booleans: bool_name
    - Inputs: input_name
    - Text Display: text_name
    - CSVs: balancesheet_name_month_year
    - Files: file_name

  IMPORT Libraries
    - csv
    - os
    - datetime

  FUNCTION check_dependencies()
    IF "business_name.txt" does not exist THEN
      PROMPT user for business name
      CREATE and WRITE "business_name.txt"
    ENDIF

    IF "usr_data" directory does not exist THEN
      CREATE "usr_data" directory
    ENDIF

    READ "business_name.txt" and STORE current_business_name
  END FUNCTION

  FUNCTION clear_screen()
    IF OS is POSIX THEN
      EXECUTE 'clear' command
    ELSE
      EXECUTE 'cls' command
    ENDIF
  END FUNCTION

  FUNCTION main_menu()
    CALL clear_screen()
    DISPLAY main menu options:
      - Create new balance sheet
      - View/edit balance sheets
      - Add transaction to balance sheet
      - Exit program

    PROMPT user for menu choice
    SWITCH menu choice:
      CASE 1: CALL new_sheet()
      CASE 2: CALL view_sheets()
      CASE 3: CALL add_transaction()
      CASE 4: EXIT program
      DEFAULT: CALL main_menu()
    END SWITCH
  END FUNCTION

  FUNCTION get_date()
    STORE current month and year
  END FUNCTION

  FUNCTION check_existing_sheet(month, year)
    SET filename = "usr_data/" + month + "_" + year + "_balance_sheet.csv"
    IF file exists THEN
      INCREMENT a counter suffix (e.g., "_001", "_002") UNTIL unique filename is found
      RETURN unique filename
    ELSE
      RETURN filename
    ENDIF
  END FUNCTION

  FUNCTION new_sheet()
    CALL clear_screen()
    CALL get_date()

    PROMPT user for:
      - Number of assets
      - Number of liabilities
      - Number of equity entities

    INITIALIZE empty lists for:
      - Asset names
      - Liability names
      - Equity entity names
      - Opening balances

    FOR each asset:
      PROMPT user for asset name and STORE in list
    END FOR

    FOR each liability:
      PROMPT user for liability name and STORE in list
    END FOR

    FOR each equity entity:
      PROMPT user for entity name and STORE in list
    END FOR

    FOR each item in assets, liabilities, and equity entities:
      PROMPT user for opening balance and STORE in list
    END FOR

    CALL check_existing_sheet(month, year) to GET filename
    CREATE CSV file with:
      - Categories (Assets, Liabilities, Equity)
      - Names of items
      - Opening balances
  END FUNCTION

  FUNCTION view_sheets()
    DISPLAY list of CSV files in "usr_data"
    PROMPT user to select a file
    OPEN and DISPLAY selected CSV file
  END FUNCTION

  FUNCTION add_transaction()
    DISPLAY list of CSV files in "usr_data"
    PROMPT user to select a file
    PROMPT user for:
      - Transaction type (Asset, Liability, Equity)
      - Name of item
      - Amount
    APPEND transaction details to the selected file
  END FUNCTION

  CALL check_dependencies()
  CALL main_menu()

END Program

Subtracting 2 lists respectively:
https://stackoverflow.com/questions/534855/subtracting-2-lists-in-python

'''