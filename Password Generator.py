import random
import string
import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import Tk, Label, Button, Entry, Checkbutton, IntVar
from ttkthemes import ThemedTk
import pyperclip
# Main logic
def generate_password():
    length = int(length_entry.get())
    use_numbers = numbers_var.get()
    use_symbols = symbols_var.get()

    if length <= 0:
        messagebox.showerror("Error", "Password length must be greater than zero.")
        return

    chars = string.ascii_letters
    if use_numbers:
        chars += string.digits
    if use_symbols:
        chars += string.punctuation

    password = ''.join(random.choice(chars) for _ in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)
    pyperclip.copy(password)  # Copy password to clipboard
    update_strength(password)

def check_strength(password):
    if len(password) < 8:
        return "Weak", "red"
    elif len(password) < 12:
        return "Medium", "orange"
    else:
        return "Strong", "green"

def update_strength(password):
    strength, color = check_strength(password)
    strength_label.config(text=f"Strength: {strength}", foreground=color)
#GUI Creation
root = ThemedTk(theme="arc")  # Change theme as per preference
root.title("Password Generator")

main_frame = ttk.Frame(root, padding="20")
main_frame.grid(row=0, column=0, sticky="nsew")

# Widgets
length_label = ttk.Label(main_frame, text="Password Length:")
length_entry = ttk.Entry(main_frame)
length_entry.insert(0, "12")  # Default length
numbers_var = tk.BooleanVar()
numbers_check = ttk.Checkbutton(main_frame, text="Include Numbers", variable=numbers_var)
symbols_var = tk.BooleanVar()
symbols_check = ttk.Checkbutton(main_frame, text="Include Symbols", variable=symbols_var)
generate_button = ttk.Button(main_frame, text="Generate Password", command=generate_password)
password_label = ttk.Label(main_frame, text="Generated Password:")
password_entry = ttk.Entry(main_frame, width=30)
password_entry.bind("<KeyRelease>", lambda event: update_strength(password_entry.get()))
strength_label = ttk.Label(main_frame, text="Strength: ", font=('Helvetica', 10, 'bold'))

# Grid layout
length_label.grid(row=0, column=0, sticky="w", padx=5, pady=5)
length_entry.grid(row=0, column=1, padx=5, pady=5)
numbers_check.grid(row=1, column=0, columnspan=2, sticky="w", padx=5, pady=5)
symbols_check.grid(row=2, column=0, columnspan=2, sticky="w", padx=5, pady=5)
generate_button.grid(row=3, column=0, columnspan=2, pady=5)
password_label.grid(row=4, column=0, sticky="w", padx=5, pady=5)
password_entry.grid(row=4, column=1, padx=5, pady=5)
strength_label.grid(row=5, column=0, columnspan=2, sticky="w", padx=5, pady=5)

# Run the main event loop
root.mainloop()
