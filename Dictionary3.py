# 21. Create a dictionary containing numbers from 1 to 10 as keys and their squares as values

squares = {}

for i in range(1, 11):
    squares[i] = i ** 2

print("Numbers and their squares:")
print(squares)


# 22. Create a dictionary containing numbers from 1 to 20 as keys and squares as values, only for even numbers

squares = {}

for i in range(1, 21):
    if i % 2 == 0:
        squares[i] = i ** 2

print("Even numbers and their squares:")
print(squares)


# 23. Given a list of numbers, create a dictionary containing each unique number and its frequency

numbers = [1, 2, 3, 2, 4, 1, 3, 2, 5, 4]

frequency = {}

for num in numbers:
    frequency[num] = frequency.get(num, 0) + 1

print("Number frequency:")
print(frequency)


# 24. Create a dictionary containing integers from 1 to 10 and their cubes

cubes = {}

for i in range(1, 11):
    cubes[i] = i ** 3

print("Numbers and their cubes:")
print(cubes)


# 25. Student dictionary operations: Add, Update, Delete, Search, Display, Highest, Average

students = {
    "Rahul": 85,
    "Amit": 75,
    "Priya": 95
}

# Add a student
name = input("Enter student name to add: ")
marks = int(input("Enter marks: "))
students[name] = marks

# Update marks
name = input("Enter student name to update: ")
if name in students:
    marks = int(input("Enter new marks: "))
    students[name] = marks
else:
    print("Student not found")

# Delete a student
name = input("Enter student name to delete: ")
if name in students:
    del students[name]
else:
    print("Student not found")

# Search for a student
name = input("Enter student name to search: ")
if name in students:
    print("Marks:", students[name])
else:
    print("Student not found")

# Display all students
print("\nAll students:")
for name, marks in students.items():
    print(name, ":", marks)

# Find highest marks
if students:
    highest = max(students.values())
    print("\nHighest marks:", highest)

# Calculate average
if students:
    average = sum(students.values()) / len(students)
    print("Average marks:", average)


# 26. Employee names and salaries: Highest, Lowest, Average, and salaries above ₹50,000

employees = {
    "Rahul": 45000,
    "Amit": 60000,
    "Priya": 75000,
    "Neha": 50000,
    "Rohan": 80000
}

highest = max(employees.values())
lowest = min(employees.values())
average = sum(employees.values()) / len(employees)

print("Highest salary:", highest)
print("Lowest salary:", lowest)
print("Average salary:", average)

print("\nEmployees earning more than ₹50,000:")
for name, salary in employees.items():
    if salary > 50000:
        print(name, ":", salary)


# 27. Product dictionary operations: Add, Update, Delete, Search, and Display products below quantity 10

products = {
    "Laptop": 15,
    "Mouse": 8,
    "Keyboard": 12,
    "Monitor": 5
}

# Add a product
name = input("Enter product name to add: ")
quantity = int(input("Enter quantity: "))
products[name] = quantity

# Update quantity
name = input("Enter product name to update: ")
if name in products:
    quantity = int(input("Enter new quantity: "))
    products[name] = quantity
else:
    print("Product not found")

# Delete a product
name = input("Enter product name to delete: ")
if name in products:
    del products[name]
else:
    print("Product not found")

# Search for a product
name = input("Enter product name to search: ")
if name in products:
    print("Quantity:", products[name])
else:
    print("Product not found")

# Display products with quantity below 10
print("\nProducts with quantity below 10:")
for name, quantity in products.items():
    if quantity < 10:
        print(name, ":", quantity)


# 28. Contact dictionary: Add, Search, Update, Delete, and Display contacts

contacts = {
    "Rahul": "9876543210",
    "Amit": "9876501234"
}

# Add contact
name = input("Enter contact name to add: ")
phone = input("Enter phone number: ")
contacts[name] = phone

# Search contact
name = input("Enter contact name to search: ")
if name in contacts:
    print("Phone number:", contacts[name])
else:
    print("Contact not found")

# Update contact
name = input("Enter contact name to update: ")
if name in contacts:
    phone = input("Enter new phone number: ")
    contacts[name] = phone
else:
    print("Contact not found")

# Delete contact
name = input("Enter contact name to delete: ")
if name in contacts:
    del contacts[name]
else:
    print("Contact not found")

# Display all contacts
print("\nAll contacts:")
for name, phone in contacts.items():
    print(name, ":", phone)


# 29. Book dictionary: Add, Search, Remove, Display, and Count total books

books = {
    101: "Python Programming",
    102: "Data Structures",
    103: "Database Management"
}

# Add a book
book_id = int(input("Enter book ID to add: "))
book_name = input("Enter book name: ")
books[book_id] = book_name

# Search a book
book_id = int(input("Enter book ID to search: "))
if book_id in books:
    print("Book name:", books[book_id])
else:
    print("Book not found")

# Remove a book
book_id = int(input("Enter book ID to remove: "))
if book_id in books:
    del books[book_id]
else:
    print("Book not found")

# Display all books
print("\nAll books:")
for book_id, book_name in books.items():
    print(book_id, ":", book_name)

# Count total books
print("Total books:", len(books))


# 30. Group students according to their department

students = {
    "Rahul": "Computer Science",
    "Amit": "Mechanical",
    "Priya": "Computer Science",
    "Neha": "Electrical",
    "Rohan": "Mechanical"
}

departments = {}

for student, department in students.items():
    if department not in departments:
        departments[department] = []

    departments[department].append(student)

print("Students grouped by department:")

for department, student_list in departments.items():
    print(department, ":", student_list)