import tkinter as tk
from tkinter import messagebox

def click(event):
    """Handles button clicks."""
    global expression
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(expression)
            input_var.set(result)
            expression = str(result)
        except Exception as e:
            messagebox.showerror("Error", "Invalid Input")
            expression = ""
            input_var.set("")
    elif text == "C":
        expression = ""
        input_var.set("")
    else:
        expression += text
        input_var.set(expression)

# Initialize the main window
root = tk.Tk()
root.title("Graphic Calculator")
root.geometry("300x400")

# Global variables
expression = ""
input_var = tk.StringVar()

# Input field
input_field = tk.Entry(root, textvar=input_var, font="Arial 20", justify="right")
input_field.pack(fill=tk.BOTH, ipadx=8, pady=10, padx=10)

# Button frame
button_frame = tk.Frame(root)
button_frame.pack()

# Button layout
buttons = [
    "7", "8", "9", "+",
    "4", "5", "6", "-",
    "1", "2", "3", "*",
    "C", "0", "=", "/"
]

# Create buttons dynamically
for i, button_text in enumerate(buttons):
    btn = tk.Button(button_frame, text=button_text, font="Arial 15", relief="ridge", height=2, width=5)
    btn.grid(row=i // 4, column=i % 4, padx=5, pady=5)
    btn.bind("<Button-1>", click)

# Run the application
root.mainloop()