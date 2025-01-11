# BSCreator
---
### A terminal-based lightweight balance sheet creator

![Current Version](https://img.shields.io/badge/current_version-alpha-orange)

---
## Summary and Merit of Project

Created for Computer Science 110 _IEDEC1100_

There are many programs available online that offer tools to help manage and track personal and business finances. These tools typically come with a wide array of features offered to their users, from simple budget planning to filing invoices. However, the abundance of flexibility offered in their causes too much distress for users, limiting the effectiveness of the program. This statement is backed by the Paradox of Choice, popularized by psychologist Barry Schwartz. It suggests that while having choices can increase user satisfaction to a point, offering too many options can lead to decision paralysis, increased anxiety, and reduced satisfaction.
These may include, but is not limited to:
- Make the app feel cluttered or confusing.
- Increase cognitive load, leading users to disengage.
- Reduce the likelihood of users completing desired actions (e.g., purchases, sign-ups).

BSCreator offers a simple solution to an oversaturated segment of the financial tools market. Many individuals and businesses today are unaware of their current financial position. By developing a straightforward balance sheet tool, many have the opportunity to regain soberness in their finances.

## Project Goals
- Develop a foundational understanding of independent project creation
- Manage project timelines efficiently and responsibly
- Use all skills learned (if applicable)
- Create language-independent structured pseudocode as a guideline for the program
- Challenge my current programming knowledge and explore new concepts
- Find solutions for any problems encountered while developing the program
- Find additional resources for issues

## CS 11 Skills Used
1. Basic Syntax: Variables, data types, comments, and indentation.
2. Control Structures: `if`, `elif`, `else` statements, loops (for and while).
3. Functions: Defining, calling, and passing arguments/returning values.
4. Data Structures: Lists, tuples, dictionaries, and sets.
5. String Manipulation: Slicing, formatting, and common methods.
6. File Handling: Reading from and writing to text files.
7. Error Handling: Using `try`, `except`, and `finally` blocks.
8. Modules and Libraries: Importing and using Python's standard libraries.
9. Basic Algorithms: Searching, sorting, and simple recursion.


## Main Features
- **Main Menu** - for user nagivation
- **Settings** - for better end-user preference
- **Balance Sheet Creator** - the main focus of the app
- **Directory** - to view a list of all created sheets and whether they are balanced or not
- **Tutorial** - introduces the user to the concept of a balance sheet, and how to navigate through the program.

## Balance Sheet Details
All concepts and accounting principles are from Business Management 120 BEBUC1200. 
![Example Formatted Balance Sheet](https://github.com/Asensado/BSCreator/blob/ee4f64fad9569c3ddcdc8ea09a219398e2e50127/gifs/image1.jpg)


The program will navigate the user to creating a balance sheet that is viewable through spreadsheet viewers such as Excel and LibreOffice. It'll acquire data in a questionnaire type of form and ask the user the following questions:
- Amount of assets, liabilities, and equity Owners
- Names of each asset, liability, and equity owner
-  Opening balances of each asset, liability, and equity owner
- Amount of transactions for the month
- Balances added or deducted for each asset, liability and equity owner

![Sheet Creation Project Flow](https://github.com/Asensado/BSCreator/blob/7674c99b7c0446ba73076e5726b6d047bf8ca7a9/gifs/flowchart.png)

It'll then auto-sum the balances and check if the balance sheet is balanced, letting the user know.


## Libraries
BSCreator _should_ run on any python interpreter version 3.10 and above. Users may need to install all required libraries or modules using `pip install -r requirements.txt`

| Library | Description |
| ------ | ------ |
|csv|Provides functionality to read, write, and manipulate CSV (Comma-Separated Values) files. |
|os|Offers tools to interact with the operating system, such as file operations and environment management.|
|os.path|A submodule of os that provides utilities to manipulate file and directory paths.|
|datetime|Supplies classes for working with dates, times, and time intervals.|
|pickle|Allows serialization and deserialization of Python objects into a byte stream.|
|glob|Enables pattern matching and retrieval of file paths based on wildcard expressions.|
|time|Provides functions to work with time, such as delays, timestamps, and conversions.|

## Project Restrictions
_Self-imposed guidelines when developing the project_
- Use only **native** Python libraries
- Have unique and detailed error handling
- Provide clear instruction to users during balance sheet creation
- Minimize repetitive code using `functions`

_The following areas below are for end-users_
___
## System Requirements

| Operating System | Requirements |
| ------ | ------ |
| Windows | x32 or x64 running at least Windows 7 |
| macOS | running at least 10.9 |
| Linux-based | Any Linux-based OS capable with CPython 3.10 running at least 4.13|

## Installation for Windows
Download BSCreator from the [Releases Page](https://github.com/Asensado/BSCreator/releases) of this repository. 
After, create a new folder in any location you wish called `BS Holder`
![Creating a BS folder on desktop](https://github.com/Asensado/BSCreator/blob/df23a0057a479cb25f9ef6fbe3db69c493da1472/gifs/video1.gif)

From there, move the `.exe` file to the newly created folder.
All data, from your business name to created balance sheets will be found here.
You can now start the program.
___
## Compiling BSCreator
You can also compile BSCreator to run on other platforms, such as Linux-based operating systems and macOS 10.9+

First, install the latest version of [Python](https://www.python.org/downloads/) on your machine.
Open your terminal, and install PyInstaller.
```bash
pip install pyinstaller
```
Then download the latest commit of BSCreator.
Navigate to the folder location on terminal.
```bash
cd path/to/your/script
```
Run PyInstaller
```
pyinstaller --onefile BalanceSheet.py
```
Alternatively, you could use `thinker` to create a lightweight GUI version of the app, then supress the terminal window with `--console`
```
pyinstaller --onefile --noconsole BalanceSheet.py
```
---
## License
GNU General Public License v2.0

_The best things in life are free, therefore BSCreator is the best._
