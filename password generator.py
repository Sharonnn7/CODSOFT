import tkinter as tk
import random
import string

def create_password():
    try:
        length = int(length_input.get())
        if length <= 0:
            result_box.delete(0, tk.END)
            result_box.insert(0, "Enter positive number")
            return

        all_chars = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(all_chars) for _ in range(length))

        result_box.delete(0, tk.END)
        result_box.insert(0, password)
    except ValueError:
        result_box.delete(0, tk.END)
        result_box.insert(0, "Invalid input")

root = tk.Tk()
root.title("Secure Password Generator")
root.geometry("350x200")
root.configure(bg="#f0f0f0")
root.resizable(False, False)

title = tk.Label(root, text="Password Generator", font=("Helvetica", 16, "bold"), bg="#f0f0f0")
title.pack(pady=10)

length_frame = tk.Frame(root, bg="#f0f0f0")
length_frame.pack()

length_label = tk.Label(length_frame, text="Password Length:", font=("Arial", 12), bg="#f0f0f0")
length_label.pack(side=tk.LEFT)

length_input = tk.Entry(length_frame, width=5)
length_input.pack(side=tk.LEFT, padx=5)

generate_btn = tk.Button(root, text="Generate", font=("Arial", 12), command=create_password)
generate_btn.pack(pady=10)

result_box = tk.Entry(root, font=("Arial", 12), width=30, justify='center')
result_box.pack(pady=5)

root.mainloop()