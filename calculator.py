import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operator = operator_var.get()

        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 == 0:
                messagebox.showerror("Math Error", "Cannot divide by zero!")
                result_label.config(text="Result: ")
                return
            result = num1 / num2
        else:
            messagebox.showerror("Error", "Invalid operation!")
            return

        result_label.config(text=f"Result: {result}")
        result_label.update_idletasks()  # ✅ Force refresh
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")
        result_label.config(text="Result: ")

root = tk.Tk()
root.title("Smart Calculator by Sharon")
root.geometry("350x300")
root.resizable(True, True)
root.configure(bg="#f0f0f0")

tk.Label(root, text="Sharon's Smart Calculator", font=("Helvetica", 16, "bold"), bg="#f0f0f0").pack(pady=10)

tk.Label(root, text="Enter first number:", bg="#f0f0f0").pack()
entry1 = tk.Entry(root, font=("Arial", 12))
entry1.pack(pady=5)

tk.Label(root, text="Enter second number:", bg="#f0f0f0").pack()
entry2 = tk.Entry(root, font=("Arial", 12))
entry2.pack(pady=5)

tk.Label(root, text="Select Operation:", bg="#f0f0f0").pack(pady=5)
operator_var = tk.StringVar(value='+')
tk.OptionMenu(root, operator_var, '+', '-', '*', '/').pack()

tk.Button(root, text="Calculate", font=("Arial", 12, "bold"), bg="#add8e6", command=calculate).pack(pady=10)

result_label = tk.Label(root, text="Result: ", font=("Arial", 12, "bold"), bg="#f0f0f0", fg="blue")
result_label.pack(pady=5)

root.mainloop()
