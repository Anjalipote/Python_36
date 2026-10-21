# 11. Use filter() and lambda to extract positive numbers

numbers = list(map(int, input("Enter numbers: ").split()))

positive_numbers = list(filter(lambda x: x > 0, numbers))

print("Positive numbers =", positive_numbers)


# 12. Use filter() and lambda to find numbers greater than 50

numbers = list(map(int, input("Enter numbers: ").split()))

greater_numbers = list(filter(lambda x: x > 50, numbers))

print("Numbers greater than 50 =", greater_numbers)


# 13. Use filter() and lambda to find words having more than five characters

words = input("Enter words separated by space: ").split()

long_words = list(filter(lambda word: len(word) > 5, words))

print("Words having more than five characters =", long_words)


# 14. Sort words according to their length using lambda

words = input("Enter words separated by space: ").split()

sorted_words = sorted(words, key=lambda word: len(word))

print("Words sorted by length =", sorted_words)


# 15. Sort students according to their marks using lambda

students = [
    ("Rahul", 75),
    ("Priya", 90),
    ("Amit", 65),
    ("Sneha", 85)
]

sorted_students = sorted(students, key=lambda student: student[1])

print("Students sorted by marks:")
for student in sorted_students:
    print(student)


# 16. Sort employee records according to salary using lambda

employees = [
    ("Rahul", 45000),
    ("Priya", 60000),
    ("Amit", 35000),
    ("Sneha", 75000)
]

sorted_employees = sorted(employees, key=lambda employee: employee[1])

print("Employees sorted by salary:")
for employee in sorted_employees:
    print(employee)


# 17. Calculate average marks, filter students above 75, and sort students by marks

students = [
    ("Rahul", 70),
    ("Priya", 85),
    ("Amit", 60),
    ("Sneha", 95),
    ("Karan", 80)
]

average = sum(map(lambda student: student[1], students)) / len(students)

above_75 = list(filter(lambda student: student[1] > 75, students))

sorted_students = sorted(students, key=lambda student: student[1])

print("Average marks =", average)
print("Students scoring above 75 =", above_75)
print("Students sorted by marks =", sorted_students)


# 18. Process employee records using filter(), map(), and sorted()

employees = [
    ("Rahul", "IT", 45000),
    ("Priya", "HR", 60000),
    ("Amit", "IT", 55000),
    ("Sneha", "Sales", 70000)
]

high_salary = list(
    filter(lambda employee: employee[2] > 50000, employees)
)

increased_salary = list(
    map(lambda employee: (employee[0], employee[1], employee[2] * 1.10), employees)
)

sorted_employees = sorted(
    employees,
    key=lambda employee: employee[2]
)

print("Employees earning more than 50000:")
print(high_salary)

print("Salaries after 10% increase:")
print(increased_salary)

print("Employees sorted by salary:")
print(sorted_employees)


# 19. Process products using functions and lambda expressions

products = [
    ("Laptop", 50000, 2),
    ("Mouse", 800, 3),
    ("Keyboard", 1500, 2),
    ("Monitor", 12000, 1)
]

total_values = list(
    map(lambda product: (
        product[0],
        product[1] * product[2]
    ), products)
)

expensive_products = list(
    filter(lambda product: product[1] * product[2] > 1000, products)
)

sorted_products = sorted(
    products,
    key=lambda product: product[1] * product[2]
)

print("Total value of each product:")
print(total_values)

print("Products costing more than 1000:")
print(expensive_products)

print("Products sorted by total value:")
print(sorted_products)


# 20. Process words using map(), filter(), and lambda

words = input("Enter words separated by space: ").split()

word_lengths = list(
    map(lambda word: len(word), words)
)

long_words = list(
    filter(lambda word: len(word) > 5, words)
)

sorted_words = sorted(
    words,
    key=lambda word: len(word)
)

print("Length of every word =", word_lengths)
print("Words having more than five characters =", long_words)
print("Words sorted by length =", sorted_words)
