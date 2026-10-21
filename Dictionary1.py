# 1. Student details - Display all key-value pairs

student = {
    "roll_number": 101,
    "name": "Rahul",
    "department": "Computer Science",
    "marks": 85
}

for key, value in student.items():
    print(key, ":", value)


# 2. Employee information - Display value associated with a specified key

employee = {
    "id": 101,
    "name": "Amit",
    "department": "IT",
    "salary": 55000
}

key = input("Enter the key: ")

if key in employee:
    print("Value:", employee[key])
else:
    print("Key not found")


# 3. Products and prices - Add a new product

products = {
    "Laptop": 50000,
    "Mobile": 20000,
    "Keyboard": 1500,
    "Mouse": 800,
    "Monitor": 10000
}

products["Headphones"] = 2000

print("Products:", products)


# 4. Student marks - Update marks

marks = {
    "Rahul": 75,
    "Amit": 82,
    "Priya": 90,
    "Sneha": 88
}

name = input("Enter student name: ")
new_marks = int(input("Enter new marks: "))

if name in marks:
    marks[name] = new_marks
    print("Updated marks:", marks)
else:
    print("Student not found")


# 5. Cities and populations - Remove a specified city

cities = {
    "Pune": 7000000,
    "Mumbai": 20000000,
    "Delhi": 33000000,
    "Nagpur": 3000000
}

city = input("Enter city to remove: ")

if city in cities:
    del cities[city]
    print("Updated dictionary:", cities)
else:
    print("City not found")


# 6. Employee IDs and names - Check whether an employee ID exists

employees = {
    101: "Rahul",
    102: "Amit",
    103: "Priya",
    104: "Sneha"
}

emp_id = int(input("Enter employee ID: "))

if emp_id in employees:
    print("Employee ID exists")
    print("Employee Name:", employees[emp_id])
else:
    print("Employee ID does not exist")


# 7. Student records - Find total number of key-value pairs

students = {
    101: "Rahul",
    102: "Amit",
    103: "Priya",
    104: "Sneha"
}

print("Total key-value pairs:", len(students))


# 8. Dictionary - Display all keys, values and key-value pairs

student = {
    "name": "Rahul",
    "age": 20,
    "department": "Computer Science",
    "marks": 85
}

print("All keys:")
print(student.keys())

print("\nAll values:")
print(student.values())

print("\nAll key-value pairs:")
print(student.items())


# 9. Programming languages and creators - Display using a loop

languages = {
    "Python": "Guido van Rossum",
    "Java": "James Gosling",
    "C": "Dennis Ritchie",
    "JavaScript": "Brendan Eich"
}

for language, creator in languages.items():
    print(language, ":", creator)


# 10. Accept five student names and marks from the user

students = {}

for i in range(5):
    name = input("Enter student name: ")
    marks = float(input("Enter marks: "))
    students[name] = marks

print("\nStudent Dictionary:")
print(students)