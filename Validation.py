
import tkinter as tk
from tkinter import messagebox
import re

def validate_form():
    name = name_entry.get().strip()
    email = email_entry.get().strip()
    age = age_entry.get().strip()
    phone = phone_entry.get().strip()
    password = password_entry.get()
    confirm_password = confirm_entry.get()

    # Name validation
    if not name:
        messagebox.showerror("Validation Error", "Name is required!")
        return

    if not name.replace(" ", "").isalpha():
        messagebox.showerror(
            "Validation Error",
            "Name must contain letters only!"
        )
        return

    # Email validation
    email_pattern = r'^[\w.-]+@[\w.-]+\.[A-Za-z]{2,}$'
    if not re.fullmatch(email_pattern, email):
        messagebox.showerror(
            "Validation Error",
            "Please enter a valid email address!"
        )
        return

    # Age validation
    if not age.isdigit() or not (16 <= int(age) <= 100):
        messagebox.showerror(
            "Validation Error",
            "Age must be between 16 and 100!"
        )
        return

    # Phone validation
    if not re.fullmatch(r'[0-9]{10}', phone):
        messagebox.showerror(
            "Validation Error",
            "Phone number must contain exactly 10 digits!"
        )
        return

    # Password validation
    if len(password) < 8:
        messagebox.showerror(
            "Validation Error",
            "Password must be at least 8 characters!"
        )
        return

    # Confirm password validation
    if password != confirm_password:
        messagebox.showerror(
            "Validation Error",
            "Passwords do not match!"
        )
        return

    messagebox.showinfo(
        "Success",
        "Registration form submitted successfully!"
    )
    clear_form()


def clear_form():
    name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)
    confirm_entry.delete(0, tk.END)


# Create main window
root = tk.Tk()
root.title("Student Registration - Validation Form")
root.geometry("420x470")
root.resizable(False, False)

tk.Label(
    root,
    text="Student Registration Form",
    font=("Arial", 16, "bold"),
    fg="blue"
).pack(pady=15)

form = tk.Frame(root)
form.pack(pady=5)

# Name
tk.Label(form, text="Full Name:").grid(
    row=0, column=0, sticky="w", padx=10, pady=8
)
name_entry = tk.Entry(form, width=27)
name_entry.grid(row=0, column=1, padx=10, pady=8)

# Email
tk.Label(form, text="Email:").grid(
    row=1, column=0, sticky="w", padx=10, pady=8
)
email_entry = tk.Entry(form, width=27)
email_entry.grid(row=1, column=1, padx=10, pady=8)

# Age
tk.Label(form, text="Age:").grid(
    row=2, column=0, sticky="w", padx=10, pady=8
)
age_entry = tk.Entry(form, width=27)
age_entry.grid(row=2, column=1, padx=10, pady=8)

# Phone
tk.Label(form, text="Phone:").grid(
    row=3, column=0, sticky="w", padx=10, pady=8
)
phone_entry = tk.Entry(form, width=27)
phone_entry.grid(row=3, column=1, padx=10, pady=8)

# Password
tk.Label(form, text="Password:").grid(
    row=4, column=0, sticky="w", padx=10, pady=8
)
password_entry = tk.Entry(form, width=27, show="*")
password_entry.grid(row=4, column=1, padx=10, pady=8)

# Confirm password
tk.Label(form, text="Confirm Password:").grid(
    row=5, column=0, sticky="w", padx=10, pady=8
)
confirm_entry = tk.Entry(form, width=27, show="*")
confirm_entry.grid(row=5, column=1, padx=10, pady=8)

# Buttons
tk.Button(
    root,
    text="Submit",
    command=validate_form,
    bg="green",
    fg="white",
    width=12
).pack(pady=12)

tk.Button(
    root,
    text="Clear",
    command=clear_form,
    width=12
).pack()

root.mainloop()
