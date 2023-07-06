# Expense Tracker

Expense Tracker is a simple application that helps you track your expenses. It allows you to record transactions with a description and amount, automatically categorize them, and store them in a CSV file.

## Features

- Record transactions with date, description, and amount
- Categorize transactions based on description
- Store transactions in a CSV file
- User-friendly interface

## Usage

1. Enter a description of the expense in the "Expense Description" field.
2. Enter the amount of the expense in the "Expense Amount" field.
3. Click the "Track Expense" button to record the transaction.
4. The transaction will be categorized automatically based on the description.
5. The transaction will be stored in the `expenses.csv` file.
6. A message box will appear confirming the successful recording of the transaction.

## Customization

You can customize the expense categorization logic by modifying the `categorize_transaction` function in the code. The provided example categorizes food-related expenses as "Food", travel-related expenses as "Travel", and all other expenses as "Other". Feel free to modify this logic to suit your needs.
