import csv
import datetime
import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
import os
import math

description_entry = None
amount_entry = None

def record_transaction(date, description, category, amount):
    with open('expenses.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, description, category, amount])

def categorize_transaction(description):
    # Implement your categorization logic here
    # You can use conditional statements or machine learning techniques to categorize the transaction based on the description
    # Example: categorize food-related expenses as "Food", travel-related expenses as "Travel", etc.
    if 'food' in description.lower():
        return 'Food'
    elif 'travel' in description.lower():
        return 'Travel'
    else:
        return 'Other'

def track_expenses():
    date = datetime.datetime.now().strftime('%Y-%m-%d')
    description = description_entry.get()
    amount = float(amount_entry.get())
    category = categorize_transaction(description)
    record_transaction(date, description, category, amount)
    messagebox.showinfo('Expense Tracker', 'Transaction recorded successfully!')
    description_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)

def create_ui():
    global description_entry, amount_entry

    window = tk.Tk()
    window.title('Expense Tracker')

    # Get screen width and height
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # Calculate the dimensions for the UI
    ui_width = math.floor(screen_width * 2 / 3)
    ui_height = math.floor(screen_height * 2 / 3)

    # Calculate the position for the UI to be centered
    x_position = math.floor((screen_width - ui_width) / 2)
    y_position = math.floor((screen_height - ui_height) / 2)

    # Set the window dimensions and position
    window.geometry(f"{ui_width}x{ui_height}+{x_position}+{y_position}")

    # Add a little pig image
    current_dir = os.path.dirname(os.path.abspath(__file__))
    pig_image_path = os.path.join(current_dir, 'pig.png')
    pig_image = ImageTk.PhotoImage(Image.open(pig_image_path).resize((200, 200)))
    pig_label = tk.Label(window, image=pig_image)
    pig_label.pack()

    description_label = tk.Label(window, text='Description:', font=('Arial', 14))
    description_label.pack()
    description_entry = tk.Entry(window, font=('Arial', 12))
    description_entry.pack()

    amount_label = tk.Label(window, text='Amount:', font=('Arial', 14))
    amount_label.pack()
    amount_entry = tk.Entry(window, font=('Arial', 12))
    amount_entry.pack()

    track_button = tk.Button(window, text='Track Expense', command=track_expenses, font=('Arial', 14))
    track_button.pack()

    window.mainloop()

def main():
    create_ui()

if __name__ == '__main__':
    main()