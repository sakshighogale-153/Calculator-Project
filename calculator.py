
import tkinter as tk

# 1. Setup Global Variables (Use simple names)
first_num = 0.0
math_operator = ""

# 2. Setup the Window
root = tk.Tk()
root.title("My Simple Calculator")

# 3. Create the Screen (Define this BEFORE the functions)
screen = tk.Entry(root, width=20, font=("Arial", 16), borderwidth=5)
screen.grid(row=0, column=0, columnspan=4)

# 4. Functions for Logic
def click_button(number):
    current = screen.get()
    screen.delete(0, tk.END)
    screen.insert(0, str(current) + str(number))

def clear_button():
    screen.delete(0, tk.END)

def set_math(op):
    global first_num
    global math_operator
    first_num = float(screen.get())
    math_operator = op
    screen.delete(0, tk.END)

def get_total():
    global first_num
    global math_operator
    second_num = float(screen.get())
    screen.delete(0, tk.END)
    
    # Manual Logic (No eval used)
    if math_operator == "+":
        screen.insert(0, first_num + second_num)
    if math_operator == "-":
        screen.insert(0, first_num - second_num)
    if math_operator == "*":
        screen.insert(0, first_num * second_num)
    if math_operator == "/":
        if second_num != 0:
            screen.insert(0, first_num / second_num)
        else:
            screen.insert(0, "Error")

# 5. Buttons (Simplified for beginner look)
tk.Button(root, text="1", padx=20, pady=20, command=lambda: click_button(1)).grid(row=1, column=0)
tk.Button(root, text="2", padx=20, pady=20, command=lambda: click_button(2)).grid(row=1, column=1)
tk.Button(root, text="3", padx=20, pady=20, command=lambda: click_button(3)).grid(row=1, column=2)
tk.Button(root, text="+", padx=20, pady=20, command=lambda: set_math("+")).grid(row=1, column=3)

tk.Button(root, text="4", padx=20, pady=20, command=lambda: click_button(4)).grid(row=2, column=0)
tk.Button(root, text="5", padx=20, pady=20, command=lambda: click_button(5)).grid(row=2, column=1)
tk.Button(root, text="6", padx=20, pady=20, command=lambda: click_button(6)).grid(row=2, column=2)
tk.Button(root, text="-", padx=20, pady=20, command=lambda: set_math("-")).grid(row=2, column=3)

tk.Button(root, text="7", padx=20, pady=20, command=lambda: click_button(7)).grid(row=3, column=0)
tk.Button(root, text="8", padx=20, pady=20, command=lambda: click_button(8)).grid(row=3, column=1)
tk.Button(root, text="9", padx=20, pady=20, command=lambda: click_button(9)).grid(row=3, column=2)
tk.Button(root, text="*", padx=20, pady=20, command=lambda: set_math("*")).grid(row=3, column=3)

tk.Button(root, text="C", padx=20, pady=20, command=clear_button).grid(row=4, column=0)
tk.Button(root, text="0", padx=20, pady=20, command=lambda: click_button(0)).grid(row=4, column=1)
tk.Button(root, text="=", padx=20, pady=20, command=get_total).grid(row=4, column=2)
tk.Button(root, text="/", padx=20, pady=20, command=lambda: set_math("/")).grid(row=4, column=3)

root.mainloop()

