# Troubleshooting
BSCreator is made to handle almost any errors that may come its way. However, one cannot account for the array of errors a program can have. Below are some troubleshooting tips you may come across.


## Permissions Error

This error occurs when you may not have the proper permissions to run this program. BSCreator often accesses files to read and edit them, and needs proper permissions to do so.

### Solution:

Ensure you are running the program with the necessary permissions. On some systems, you may need to run it as an administrator.

If the issue persists, check that the directory or files being accessed are not restricted or read-only.

This problem can also occur if you have the file open. When you open the file, the program viewing it locks the file, making it inaccessible to BSCreator and other programs. Try closing the file and try again.





## File Not Found Error

This error may occur if the program is unable to locate a file, such as a configuration file or balance sheet.

### Solution:

Verify that the required files (e.g., config.ini) are present in the same directory as the program.

If the file is missing, restart the program. BSCreator will recreate default files if necessary.

Ensure the specified directory in the settings menu exists and is accessible.





## ValueError: Enter Numbers Only

This occurs if you input text or invalid characters when the program is expecting a numerical value.

### Solution:

Re-enter the input, ensuring it is a valid number.

Avoid including special characters (e.g., $, ,, .) unless part of a number (e.g., -100.50).





## CSV File Corruption or Errors

If a balance sheet file has been modified manually or corrupted, the program may fail to read it correctly.

### Solution:

Avoid editing the CSV files directly unless you know the required format.

If a file is corrupted, consider creating a new balance sheet using the program.

Keep backups of your balance sheets in case of accidental corruption.





## Program Freezes or Crashes

This might occur if the program encounters a loop or unexpected data.

### Solution:

Restart the program and try again.

Ensure you are providing valid inputs. For example, enter realistic numbers for balances and transactions.

If the issue persists, check for updates or contact the developer for support.





## Directory Not Found

This error may occur if the program’s save directory has been deleted or moved.

### Solution:

Go to the settings menu and update the save directory.

Ensure the new directory exists and is accessible by the program.





## KeyboardInterrupt Error

This occurs if you press Ctrl+C unexpectedly during critical processes.

### Solution:

Avoid using Ctrl+C unless prompted by the program.

Restart the program if necessary, and retry the interrupted action.



---

For persistent issues, consult the program documentation or [create a new issue](https://github.com/Asensado/BSCreator/issues).
