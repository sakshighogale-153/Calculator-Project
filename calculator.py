# Import tkinter
import tkinter as tk

# Create main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x400")

# Entry box (display screen)
entry = tk.Entry(root, width=20, font=("Arial", 20), borderwidth=5, relief="ridge")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)


# Function to click numbers
def click_button(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))


# Function to clear screen
def clear():
    entry.delete(0, tk.END)


# Function to calculate result
def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")


# Create buttons
buttons = [
    ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3),
    ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),
    ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),
    ('0',4,0), ('.',4,1), ('C',4,2), ('+',4,3),
]

# Place buttons on screen
for (text, row, col) in buttons:
    if text == "C":
        button = tk.Button(root, text=text, padx=20, pady=20,
                           command=clear)
    else:
        button = tk.Button(root, text=text, padx=20, pady=20,
                           command=lambda t=text: click_button(t))

    button.grid(row=row, column=col)

# Equal button
equal_button = tk.Button(root, text="=", padx=20, pady=20, command=calculate)
equal_button.grid(row=5, column=0, columnspan=4, sticky="nsew")

# Run the app
root.mainloop()