
import tkinter as tk
from tkinter import messagebox

def register():
    name = entry_name.get()
    roll = entry_roll.get()
    age = entry_age.get()
    course = course_var.get()
    gender = gender_var.get()
    email = entry_email.get()

    if not name or not roll or not age or not email:
        messagebox.showerror("Error", "Please fill all fields!")
        return

    messagebox.showinfo(
        "Registration Successful",
        f"Name: {name}\nRoll No: {roll}\nAge: {age}\n"
        f"Course: {course}\nGender: {gender}\nEmail: {email}"
    )

root = tk.Tk()
root.title("Student Registration Form")
root.geometry("400x500")
root.configure(bg="lightblue")

tk.Label(
    root, text="Student Registration Form",
    font=("Arial", 18, "bold"), bg="lightblue"
).pack(pady=15)

tk.Label(root, text="Student Name", bg="lightblue").pack()
entry_name = tk.Entry(root, width=30)
entry_name.pack(pady=5)

tk.Label(root, text="Roll Number", bg="lightblue").pack()
entry_roll = tk.Entry(root, width=30)
entry_roll.pack(pady=5)

tk.Label(root, text="Age", bg="lightblue").pack()
entry_age = tk.Entry(root, width=30)
entry_age.pack(pady=5)

tk.Label(root, text="Gender", bg="lightblue").pack()
gender_var = tk.StringVar(value="Male")
tk.OptionMenu(root, gender_var, "Male", "Female", "Other").pack()

tk.Label(root, text="Course", bg="lightblue").pack()
course_var = tk.StringVar(value="Computer Science")
tk.OptionMenu(
    root, course_var,
    "Computer Science", "IT", "Mechanical", "Civil", "Electrical"
).pack()

tk.Label(root, text="Email", bg="lightblue").pack()
entry_email = tk.Entry(root, width=30)
entry_email.pack(pady=5)

tk.Button(
    root, text="Register",
    command=register, bg="green", fg="white",
    font=("Arial", 12, "bold")
).pack(pady=20)

root.mainloop()

