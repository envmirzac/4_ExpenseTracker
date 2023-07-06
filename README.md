Expense Tracker

The Expense Tracker is a Python program that allows users to track their expenses by recording and categorizing transactions. It provides a graphical user interface (GUI) using the Tkinter library and stores the transactions in a CSV file.

Features:

Record transactions with the date, description, category, and amount
Automatically categorize transactions based on the description
Display a message after recording a transaction
GUI with input fields for description and amount
Little pig image as a visual element
Prerequisites:

Python 3.x should be installed on your system.
The required libraries (csv, datetime, tkinter, PIL) should be installed. You can install them using pip.
Usage:

Clone or download the project repository to your local machine.

Make sure you have the required libraries installed by running the following command in your terminal:

pip install csv datetime pillow
Open the expense_tracker.py file in a text editor.

Customize the categorize_transaction function to implement your own categorization logic based on the transaction description.

Save the changes to the expense_tracker.py file.

Open a terminal or command prompt and navigate to the directory where the expense_tracker.py file is located.

Run the program by executing the following command:

Copy code
python expense_tracker.py
The Expense Tracker GUI will open. Enter the description and amount for each expense and click the "Track Expense" button to record the transaction.

After recording a transaction, a message will be displayed indicating the successful recording of the transaction.

Customization:

You can customize the program by modifying the categorization logic in the categorize_transaction function to suit your specific needs.
You can also modify the GUI elements, such as the window title, image, and layout, by editing the corresponding code in the create_ui function.
Note: Make sure to provide a proper path to the "pig.png" image file or replace it with your own image file. The image should be located in the same directory as the expense_tracker.py file.

Enjoy tracking your expenses with the Expense Tracker!
