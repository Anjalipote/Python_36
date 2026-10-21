# 21. Calculate the total bill after applying a discount

def total_bill(prices, quantities):
    total = 0

    for i in range(len(prices)):
        total = total + (prices[i] * quantities[i])

    if total >= 5000:
        discount = total * 0.20
    elif total >= 2000:
        discount = total * 0.10
    else:
        discount = total * 0.05

    return total - discount

prices = list(map(float, input("Enter item prices: ").split()))
quantities = list(map(int, input("Enter quantities: ").split()))

print("Final Bill =", total_bill(prices, quantities))


# 22. Find minimum, maximum, sum, and average of a list

def list_operations(numbers):
    minimum = numbers[0]
    maximum = numbers[0]
    total = 0

    for num in numbers:
        if num < minimum:
            minimum = num

        if num > maximum:
            maximum = num

        total = total + num

    average = total / len(numbers)
    return minimum, maximum, total, average

numbers = list(map(int, input("Enter numbers: ").split()))
minimum, maximum, total, average = list_operations(numbers)
print("Minimum =", minimum)
print("Maximum =", maximum)
print("Sum =", total)
print("Average =", average)


# 23. Process student records

def calculate_student(marks):
    total = sum(marks)
    percentage = total / 5

    if percentage >= 90:
        grade = "A"
    elif percentage >= 80:
        grade = "B"
    elif percentage >= 70:
        grade = "C"
    elif percentage >= 60:
        grade = "D"
    elif percentage >= 50:
        grade = "E"
    else:
        grade = "F"

    return total, percentage, grade


students = []

n = int(input("Enter number of students: "))

for i in range(n):
    name = input("Enter name: ")
    roll = input("Enter roll number: ")
    marks = list(map(float, input("Enter 5 marks: ").split()))

    total, percentage, grade = calculate_student(marks)

    students.append({
        "name": name,
        "roll": roll,
        "marks": marks,
        "total": total,
        "percentage": percentage,
        "grade": grade
    })

total_percentage = 0

for student in students:
    total_percentage += student["percentage"]

class_average = total_percentage / n

highest = students[0]
lowest = students[0]

for student in students:
    if student["percentage"] > highest["percentage"]:
        highest = student

    if student["percentage"] < lowest["percentage"]:
        lowest = student

for student in students:
    print(
        student["name"],
        student["roll"],
        student["total"],
        student["percentage"],
        student["grade"]
    )

print("Class Average =", class_average)
print("Highest Scorer =", highest["name"])
print("Lowest Scorer =", lowest["name"])


# 24. Bank management system

balance = 0
transactions = []

def deposit(amount):
    global balance
    balance += amount
    transactions.append("Deposited: " + str(amount))

def withdrawal(amount):
    global balance

    if amount <= balance:
        balance -= amount
        transactions.append("Withdrawn: " + str(amount))
        print("Withdrawal successful")
    else:
        print("Insufficient balance")


def balance_enquiry():
    print("Balance =", balance)
    
def transaction_history():
    print("Transaction History:")

    for transaction in transactions:
        print(transaction)


deposit(5000)
withdrawal(1000)
balance_enquiry()
transaction_history()


# 25. Library management system

books = {}

def add_book(book_id, book_name):
    books[book_id] = {
        "name": book_name,
        "available": True
    }

def issue_book(book_id):
    if book_id in books:
        if books[book_id]["available"]:
            books[book_id]["available"] = False
            print("Book issued")
        else:
            print("Book is already issued")
    else:
        print("Book not found")

def return_book(book_id):
    if book_id in books:
        books[book_id]["available"] = True
        print("Book returned")
    else:
        print("Book not found")

def search_book(book_name):
    for book_id, book in books.items():
        if book["name"].lower() == book_name.lower():
            print("Book found:", book_id, book["name"])
            return

    print("Book not found")

def display_available_books():
    print("Available Books:")

    for book_id, book in books.items():
        if book["available"]:
            print(book_id, book["name"])


add_book(1, "Python")
add_book(2, "Java")
add_book(3, "C Programming")

issue_book(1)
return_book(1)
search_book("Python")
display_available_books()


# 26. Electricity bill with fixed charges, taxes, and discounts

def calculate_bill(units):
    if units <= 100:
        energy_charge = units * 5
    elif units <= 200:
        energy_charge = (100 * 5) + ((units - 100) * 7)
    else:
        energy_charge = (100 * 5) + (100 * 7) + ((units - 200) * 10)

    fixed_charge = 100
    subtotal = energy_charge + fixed_charge

    if units > 300:
        discount = subtotal * 0.05
    else:
        discount = 0

    taxable_amount = subtotal - discount
    tax = taxable_amount * 0.05

    final_bill = taxable_amount + tax

    return final_bill


units = float(input("Enter units consumed: "))
print("Final Electricity Bill =", calculate_bill(units))


# 27. Hospital billing system

def consultation_charges(category):
    if category == "senior":
        return 300
    elif category == "child":
        return 200
    else:
        return 500

def laboratory_charges():
    return 1000

def medicine_charges():
    return 1500

def room_charges():
    return 2000

def final_bill(category):
    consultation = consultation_charges(category)
    laboratory = laboratory_charges()
    medicine = medicine_charges()
    room = room_charges()

    total = consultation + laboratory + medicine + room

    if category == "senior":
        discount = total * 0.20
    elif category == "child":
        discount = total * 0.10
    else:
        discount = 0

    return total - discount


category = input("Enter patient category (senior/child/general): ").lower()
print("Final Hospital Bill =", final_bill(category))


# 28. Product invoice with coupon and GST

products = []


def add_product(name, price, quantity):
    products.append({
        "name": name,
        "price": price,
        "quantity": quantity
    })

def remove_product(name):
    for product in products:
        if product["name"] == name:
            products.remove(product)
            return

def calculate_subtotal():
    subtotal = 0

    for product in products:
        subtotal += product["price"] * product["quantity"]

    return subtotal

def apply_coupon(subtotal, coupon):
    if coupon == "SAVE10":
        return subtotal * 0.10
    elif coupon == "SAVE20":
        return subtotal * 0.20
    else:
        return 0

def calculate_gst(amount):
    return amount * 0.18

def generate_invoice(coupon):
    subtotal = calculate_subtotal()
    discount = apply_coupon(subtotal, coupon)
    amount = subtotal - discount
    gst = calculate_gst(amount)
    final_amount = amount + gst

    print("Subtotal =", subtotal)
    print("Discount =", discount)
    print("GST =", gst)
    print("Final Amount =", final_amount)


add_product("Laptop", 50000, 1)
add_product("Mouse", 1000, 2)
generate_invoice("SAVE10")


# 29. Recursive binary search

def binary_search(numbers, target, low, high):
    if low > high:
        return -1

    mid = (low + high) // 2

    if numbers[mid] == target:
        return mid
    
    if target < numbers[mid]:
        return binary_search(numbers, target, low, mid - 1)
    return binary_search(numbers, target, mid + 1, high)


numbers = list(map(int, input("Enter sorted numbers: ").split()))
target = int(input("Enter element to search: "))

result = binary_search(numbers, target, 0, len(numbers) - 1)

if result != -1:
    print("Element found at index", result)
else:
    print("Element not found")


# 30. Convert decimal to binary using recursion

def decimal_to_binary(n):
    if n == 0:
        return ""
    return decimal_to_binary(n // 2) + str(n % 2)


n = int(input("Enter decimal number: "))

if n == 0:
    print("Binary = 0")
else:
    print("Binary =", decimal_to_binary(n))


# 31. Check palindrome using recursion

def palindrome_recursive(text, start, end):
    if start >= end:
        return True

    if text[start] != text[end]:
        return False
    return palindrome_recursive(text, start + 1, end - 1)


text = input("Enter a string: ")

if palindrome_recursive(text, 0, len(text) - 1):
    print("Palindrome")
else:
    print("Not Palindrome")


# 32. Calculator using functions passed as arguments

def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

def calculate(a, b, operation):
    return operation(a, b)


a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("Addition =", calculate(a, b, addition))
print("Subtraction =", calculate(a, b, subtraction))
print("Multiplication =", calculate(a, b, multiplication))
print("Division =", calculate(a, b, division))
