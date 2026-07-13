import tkinter as tk

root = tk.Tk()
root.title("Calculator")
root.geometry("380x500")
root.resizable(False, False)

expression = ""

display = tk.Entry(
    root,
    font=("Arial", 22),
    justify="right",
    bd=8
)
display.pack(fill="x", padx=10, pady=20)


def press(value):
    global expression
    expression += str(value)
    display.delete(0, tk.END)
    display.insert(tk.END, expression)


def clear():
    global expression
    expression = ""
    display.delete(0, tk.END)


def calculate():
    global expression
    try:
        result = str(eval(expression))
        display.delete(0, tk.END)
        display.insert(tk.END, result)
        expression = result
    except:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")
        expression = ""


button_frame = tk.Frame(root)
button_frame.pack(pady=10)

buttons = [
    ("7", 0, 0), ("8", 0, 1), ("9", 0, 2), ("/", 0, 3),
    ("4", 1, 0), ("5", 1, 1), ("6", 1, 2), ("*", 1, 3),
    ("1", 2, 0), ("2", 2, 1), ("3", 2, 2), ("-", 2, 3),
    ("0", 3, 0), (".", 3, 1), ("=", 3, 2), ("+", 3, 3),
]

for (text, row, col) in buttons:

    if text == "=":
        button = tk.Button(
            button_frame,
            text=text,
            width=6,
            height=2,
            font=("Arial", 16, "bold"),
            command=calculate
        )
    else:
        button = tk.Button(
            button_frame,
            text=text,
            width=6,
            height=2,
            font=("Arial", 16),
            command=lambda value=text: press(value)
        )

    button.grid(row=row, column=col, padx=5, pady=5)

clear_button = tk.Button(
    root,
    text="Clear",
    width=30,
    height=2,
    font=("Arial", 14),
    command=clear
)

clear_button.pack(pady=15)

root.mainloop()