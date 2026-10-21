
import tkinter as tk
from tkinter import messagebox
import csv
import os

def register_student():
    name = name_entry.get().strip()
    age = age_entry.get().strip()
    gender = gender_var.get()
    course = course_var.get()
    email = email_entry.get().strip()
    phone = phone_entry.get().strip()

    if not name or not age or not email or not phone:
        messagebox.showerror("Error", "Please fill in all fields.")
        return

    if not age.isdigit() or int(age) <= 0:
        messagebox.showerror("Error", "Please enter a valid age.")
        return

    if not course:
        messagebox.showerror("Error", "Please select a course.")
        return

    file_exists = os.path.isfile("students.csv")

    with open("students.csv", "a", newline="") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow([
                "Name", "Age", "Gender",
                "Course", "Email", "Phone"
            ])

        writer.writerow([
            name, age, gender, course, email, phone
        ])

    messagebox.showinfo(
        "Success",
        f"Registration successful!\nWelcome, {name}."
    )

    clear_form()


def clear_form():
    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    gender_var.set("Male")
    course_var.set("")
    email_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)


# Main window
root = tk.Tk()
root.title("Student Registration Form")
root.geometry("450x500")
root.resizable(False, False)

# Heading
tk.Label(
    root,
    text="Student Registration Form",
    font=("Arial", 18, "bold"),
    fg="blue"
).pack(pady=15)

# Form frame
form = tk.Frame(root)
form.pack(pady=5)

# Student name
tk.Label(form, text="Full Name:", font=("Arial", 11)).grid(
    row=0, column=0, sticky="w", padx=10, pady=8
)
name_entry = tk.Entry(form, width=28)
name_entry.grid(row=0, column=1, padx=10, pady=8)

# Age
tk.Label(form, text="Age:", font=("Arial", 11)).grid(
    row=1, column=0, sticky="w", padx=10, pady=8
)
age_entry = tk.Entry(form, width=28)
age_entry.grid(row=1, column=1, padx=10, pady=8)

# Gender
tk.Label(form, text="Gender:", font=("Arial", 11)).grid(
    row=2, column=0, sticky="w", padx=10, pady=8
)
gender_var = tk.StringVar(value="Male")
gender_menu = tk.OptionMenu(
    form, gender_var, "Male", "Female", "Other"
)
gender_menu.config(width=23)
gender_menu.grid(row=2, column=1, padx=10, pady=8)

# Course
tk.Label(form, text="Course:", font=("Arial", 11)).grid(
    row=3, column=0, sticky="w", padx=10, pady=8
)
course_var = tk.StringVar(value="")
course_menu = tk.OptionMenu(
    form, course_var,
    "BCA", "BBA", "B.Tech", "B.Sc", "MBA", "MCA"
)
course_menu.config(width=23)
course_menu.grid(row=3, column=1, padx=10, pady=8)

# Email
tk.Label(form, text="Email:", font=("Arial", 11)).grid(
    row=4, column=0, sticky="w", padx=10, pady=8
)
email_entry = tk.Entry(form, width=28)
email_entry.grid(row=4, column=1, padx=10, pady=8)

# Phone
tk.Label(form, text="Phone Number:", font=("Arial", 11)).grid(
    row=5, column=0, sticky="w", padx=10, pady=8
)
phone_entry = tk.Entry(form, width=28)
phone_entry.grid(row=5, column=1, padx=10, pady=8)

# Buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=20)

tk.Button(
    button_frame,
    text="Register",
    command=register_student,
    bg="green",
    fg="white",
    width=12
).grid(row=0, column=0, padx=10)

tk.Button(
    button_frame,
    text="Clear",
    command=clear_form,
    width=12
).grid(row=0, column=1, padx=10)

root.mainloop()
