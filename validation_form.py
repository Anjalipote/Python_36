
import tkinter as tk
from tkinter import messagebox
import re

def register():
    name = entry_name.get().strip()
    roll = entry_roll.get().strip()
    age = entry_age.get().strip()
    email = entry_email.get().strip()
    course = course_var.get()
    gender = gender_var.get()

    # Name validation
    if not name:
        messagebox.showerror("Error", "Name cannot be empty")
        return

    if not name.replace(" ", "").isalpha():
        messagebox.showerror("Error", "Name must contain only letters")
        return

    # Roll number validation
    if not roll.isdigit():
        messagebox.showerror("Error", "Roll number must be numeric")
        return

    # Age validation
    if not age.isdigit() or not (16 <= int(age) <= 60):
        messagebox.showerror("Error", "Enter a valid age (16-60)")
        return

    # Email validation
    pattern = r'^[\w.-]+@[\w.-]+\.[A-Za-z]{2,}$'
    if not re.match(pattern, email):
        messagebox.showerror("Error", "Enter a valid email address")
        return

    # Course and gender validation
    if course == "Select Course":
        messagebox.showerror("Error", "Please select a course")
        return

    if gender == "Select Gender":
        messagebox.showerror("Error", "Please select gender")
        return

    messagebox.showinfo(
        "Success",
        f"Registration Successful!\n\nName: {name}\nRoll No: {roll}"
        f"\nAge: {age}\nEmail: {email}\nCourse: {course}\nGender: {gender}"
    )

root = tk.Tk()
root.title("Student Registration Form")
root.geometry("400x550")
root.configure(bg="lightblue")

tk.Label(root, text="Student Registration Form",
         font=("Arial", 18, "bold"), bg="lightblue").pack(pady=15)

tk.Label(root, text="Student Name", bg="lightblue").pack()
entry_name = tk.Entry(root)
entry_name.pack(pady=5)

tk.Label(root, text="Roll Number", bg="lightblue").pack()
entry_roll = tk.Entry(root)
entry_roll.pack(pady=5)

tk.Label(root, text="Age", bg="lightblue").pack()
entry_age = tk.Entry(root)
entry_age.pack(pady=5)

tk.Label(root, text="Email", bg="lightblue").pack()
entry_email = tk.Entry(root)
entry_email.pack(pady=5)

tk.Label(root, text="Course", bg="lightblue").pack()
course_var = tk.StringVar(value="Select Course")
tk.OptionMenu(root, course_var, "Computer Science",
              "IT", "Mechanical", "Civil", "Electrical").pack()

tk.Label(root, text="Gender", bg="lightblue").pack()
gender_var = tk.StringVar(value="Select Gender")
tk.OptionMenu(root, gender_var, "Male", "Female", "Other").pack()

tk.Button(root, text="Register", command=register,
          bg="green", fg="white",
          font=("Arial", 12, "bold")).pack(pady=20)

root.mainloop()
