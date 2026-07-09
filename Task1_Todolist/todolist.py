import tkinter as tk
import json

root = tk.Tk()
root.title("To-Do List")
root.geometry("500x500")

tasks = []

def save_tasks():
    tasks = task_listbox.get(0, tk.END)
    with open("tasks.json", "w") as file:
        json.dump(list(tasks), file)

def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
            for task in tasks:
                task_listbox.insert(tk.END, task)
    except FileNotFoundError:
        pass

def add_task():
    task = task_entry.get().strip()

    if task:
        task_listbox.insert(tk.END, "☐ " + task)
        task_entry.delete(0, tk.END)
        save_tasks()

def edit_task():
    try:
        selected = task_listbox.curselection()[0]
        current_task = task_listbox.get(selected)

        edit_window = tk.Toplevel(root)
        edit_window.title("Edit Task")
        edit_window.geometry("300x150")

        tk.Label(edit_window, text="Edit Task:").pack(pady=5)

        edit_entry = tk.Entry(edit_window, width=30)
        edit_entry.pack(pady=5)

        edit_entry.insert(0, current_task[2:])

        def save_edit():
            new_task = edit_entry.get().strip()

            if new_task:
                status = current_task[:2]
                task_listbox.delete(selected)
                task_listbox.insert(selected, status + new_task)
                save_tasks()
                edit_window.destroy()

        tk.Button(
            edit_window,
            text="Save",
            command=save_edit
        ).pack(pady=10)

    except IndexError:
        print("Please select a task first.")

def complete_task():
    try:
        selected = task_listbox.curselection()[0]
        task = task_listbox.get(selected)

        if task.startswith("☐"):
            task = task.replace("☐", "☑", 1)
            task_listbox.delete(selected)
            task_listbox.insert(selected, task)
            save_tasks()

    except IndexError:
        print("Please select a task.")

def delete_task():
    try:
        selected = task_listbox.curselection()[0]
        task_listbox.delete(selected)
        save_tasks()

    except IndexError:
        print("Please select a task.")

head = tk.Label(
    root,
    text="To-Do List",
    font=("Arial", 22, "bold")
)
head.pack(pady=20)

task_entry = tk.Entry(
    root,
    width=40,
    font=("Arial", 14)
)
task_entry.pack(pady=10)

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

add_button = tk.Button(
    button_frame,
    text="Add",
    width=10,
    command=add_task
)

edit_button = tk.Button(
    button_frame,
    text="Edit",
    width=10,
    command=edit_task
)

complete_button = tk.Button(
    button_frame,
    text="Complete",
    width=10,
    command=complete_task
)

delete_button = tk.Button(
    button_frame,
    text="Delete",
    width=10,
    command=delete_task
)

add_button.grid(row=0, column=0, padx=5)
edit_button.grid(row=0, column=1, padx=5)
complete_button.grid(row=0, column=2, padx=5)
delete_button.grid(row=0, column=3, padx=5)

task_listbox = tk.Listbox(
    root,
    width=40,
    height=10,
    font=("Arial", 14)
)
task_listbox.pack(pady=20)

load_tasks()

root.mainloop()