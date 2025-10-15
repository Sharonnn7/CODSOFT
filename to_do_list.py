import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

def delete_task():
    try:
        selected_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_index)
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")

def clear_tasks():
    task_listbox.delete(0, tk.END)

root = tk.Tk()
root.title("To-Do List")
root.geometry("400x400")
root.resizable(False, False)
root.configure(bg="#f7f7f7")

tk.Label(root, text="My To-Do List", font=("Helvetica", 16, "bold"), bg="#f7f7f7").pack(pady=10)

task_entry = tk.Entry(root, width=35, font=("Arial", 12))
task_entry.pack(pady=10)

btn_frame = tk.Frame(root, bg="#f7f7f7")
btn_frame.pack()

add_btn = tk.Button(btn_frame, text="Add Task", width=12, command=add_task)
add_btn.grid(row=0, column=0, padx=5)

delete_btn = tk.Button(btn_frame, text="Delete Task", width=12, command=delete_task)
delete_btn.grid(row=0, column=1, padx=5)

clear_btn = tk.Button(btn_frame, text="Clear All", width=12, command=clear_tasks)
clear_btn.grid(row=0, column=2, padx=5)

task_listbox = tk.Listbox(root, width=50, height=12, font=("Arial", 11), selectbackground="#d1e7dd")
task_listbox.pack(pady=20)

root.mainloop()
