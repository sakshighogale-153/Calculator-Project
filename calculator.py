import tkinter as tk
from tkinter import messagebox

# --- 1. Window Setup ---
root = tk.Tk()
root.title("TuteDude Assignment 6")
root.geometry("300x400")

# --- 2. Global Variables (Required by Mentor) ---
first_number = 0.0
operator = ""
is_operator_clicked = False

# --- 3. Create the Entry Widget FIRST ---
# This fixes the "entry is not defined" error from your screenshot
entry = tk.Entry(root, width=15, font=('Arial', 24), borderwidth=5, justify='right')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=20)

# --- 4. Logic Functions ---
def button_click(number):
    global is_operator_clicked
    if is_operator_clicked:
        entry.delete(0, tk.END)
        entry.insert(0, str(number))
        is_operator_clicked = False
    else:
        entry.insert(tk.END, str(number))

def button_clear():
    global first_number, operator
    entry.delete(0, tk.END)
    first_number = 0.0
    operator = ""

def set_operation(op):
    global first_number, operator, is_operator_clicked
    try:
        first_number = float(entry.get())
        operator = op
        is_operator_clicked = True
    except ValueError:
        messagebox.showerror("Error", "Enter a number first")

def calculate_result():
    global first_number, operator
    try:
        second_number = float(entry.get())
        entry.delete(0, tk.END)

        if operator == "+":
            entry.insert(0, first_number + second_number)
        elif operator == "-":
            entry.insert(0, first_number - second_number)
        elif operator == "*":
            entry.insert(0, first_number * second_number)
        elif operator == "/":
            if second_number == 0:
                entry.insert(0, "Error")
            else:
                entry.insert(0, first_number / second_number)
    except Exception:
        messagebox.showerror("Error", "Invalid Input")

# --- 5. Buttons ---
btns = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

for (text, r, c) in btns:
    if text.isdigit():
        action = lambda x=text: button_click(x)
    elif text == "C":
        action = button_clear
    elif text == "=":
        action = calculate_result
    else:
        action = lambda x=text: set_operation(x)
    
    tk.Button(root, text=text, width=5, height=2, font=('Arial', 14),
              command=action).grid(row=r, column=c, padx=2, pady=2)

# --- 6. The Loop (This MUST be the last line) ---
print("The code is now running! Look for the window.")
root.mainloop()
