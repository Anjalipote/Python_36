# Q1. Student class with roll number, name, marks and percentage

class Student:
    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks

    def percentage(self):
        return sum(self.marks) / len(self.marks)

    def display(self):
        print("Roll No:", self.roll_no)
        print("Name:", self.name)
        print("Marks:", self.marks)
        print("Percentage:", self.percentage())


students = [
    Student(101, "Rahul", [80, 85, 90, 75, 88]),
    Student(102, "Priya", [90, 92, 85, 88, 95]),
    Student(103, "Amit", [70, 75, 80, 72, 78])
]

for student in students:
    student.display()
    print()


# Q2. Employee class with HRA, DA and gross salary

class Employee:
    def __init__(self, emp_id, name, basic_salary):
        self.emp_id = emp_id
        self.name = name
        self.basic_salary = basic_salary

    def hra(self):
        return self.basic_salary * 0.20

    def da(self):
        return self.basic_salary * 0.10

    def gross_salary(self):
        return self.basic_salary + self.hra() + self.da()

    def display(self):
        print("Employee ID:", self.emp_id)
        print("Name:", self.name)
        print("Basic Salary:", self.basic_salary)
        print("HRA:", self.hra())
        print("DA:", self.da())
        print("Gross Salary:", self.gross_salary())


e = Employee(101, "Rahul", 50000)
e.display()


# Q3. Rectangle class with area and perimeter

class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)


r = Rectangle(10, 5)

print("Area:", r.area())
print("Perimeter:", r.perimeter())


# Q4. Circle class with area and circumference

import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius

    def circumference(self):
        return 2 * math.pi * self.radius


c = Circle(5)

print("Area:", c.area())
print("Circumference:", c.circumference())


# Q5. Book class with details of three books

class Book:
    def __init__(self, book_id, title, author, price):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.price = price

    def display(self):
        print("Book ID:", self.book_id)
        print("Title:", self.title)
        print("Author:", self.author)
        print("Price:", self.price)


books = [
    Book(101, "Python Basics", "John", 500),
    Book(102, "Java Programming", "James", 600),
    Book(103, "C Programming", "Dennis", 450)
]

for book in books:
    book.display()
    print()


# Q6. ElectricityBill class with slab-based bill calculation

class ElectricityBill:
    def __init__(self, consumer_no, consumer_name, units):
        self.consumer_no = consumer_no
        self.consumer_name = consumer_name
        self.units = units

    def calculate_bill(self):
        units = self.units

        if units <= 100:
            bill = units * 1.5
        elif units <= 200:
            bill = 100 * 1.5 + (units - 100) * 2.5
        elif units <= 500:
            bill = 100 * 1.5 + 100 * 2.5 + (units - 200) * 4
        else:
            bill = (
                100 * 1.5
                + 100 * 2.5
                + 300 * 4
                + (units - 500) * 6
            )

        return bill

    def display(self):
        print("Consumer Number:", self.consumer_no)
        print("Consumer Name:", self.consumer_name)
        print("Units:", self.units)
        print("Electricity Bill:", self.calculate_bill())


bill = ElectricityBill(1001, "Amit", 350)
bill.display()


# Q7. MobilePhone class with specifications and discount

class MobilePhone:
    def __init__(self, brand, model, storage, price):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.price = price

    def display(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Storage:", self.storage)
        print("Price:", self.price)

    def discounted_price(self, discount):
        return self.price - self.price * discount / 100


phone = MobilePhone("Samsung", "Galaxy S24", "256 GB", 70000)

phone.display()
print("Price after discount:", phone.discounted_price(10))


# Q8. Patient class with total bill

class Patient:
    def __init__(
        self,
        patient_id,
        name,
        age,
        disease,
        consultation_fee
    ):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.disease = disease
        self.consultation_fee = consultation_fee

    def total_bill(self):
        medicine_fee = 1000
        return self.consultation_fee + medicine_fee

    def display(self):
        print("Patient ID:", self.patient_id)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Disease:", self.disease)
        print("Consultation Fee:", self.consultation_fee)
        print("Total Bill:", self.total_bill())


p = Patient(
    101,
    "Rahul",
    30,
    "Fever",
    500
)

p.display()


# Q9. ATM class with menu-driven operations

class ATM:
    def __init__(self, account_no, name, balance):
        self.account_no = account_no
        self.name = name
        self.balance = balance

    def check_balance(self):
        print("Balance:", self.balance)

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient balance")

    def display_account(self):
        print("Account Number:", self.account_no)
        print("Name:", self.name)
        print("Balance:", self.balance)


atm = ATM(1001, "Rahul", 10000)

while True:
    print("\n1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Display Account")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        atm.check_balance()

    elif choice == 2:
        amount = float(input("Enter amount: "))
        atm.deposit(amount)

    elif choice == 3:
        amount = float(input("Enter amount: "))
        atm.withdraw(amount)

    elif choice == 4:
        atm.display_account()

    elif choice == 5:
        print("Thank you!")
        break

    else:
        print("Invalid choice")


# Q10. Vehicle class with rent and return operations

class Vehicle:
    def __init__(self, vehicle_no, model, rental_rate):
        self.vehicle_no = vehicle_no
        self.model = model
        self.rental_rate = rental_rate
        self.available = True

    def rent(self):
        if self.available:
            self.available = False
            print("Vehicle rented successfully")
        else:
            print("Vehicle is not available")

    def return_vehicle(self):
        self.available = True
        print("Vehicle returned successfully")

    def rental_charges(self, days):
        return self.rental_rate * days

    def display(self):
        print("Vehicle Number:", self.vehicle_no)
        print("Model:", self.model)
        print("Rental Rate:", self.rental_rate)
        print("Available:", self.available)


vehicle = Vehicle("MH12AB1234", "Honda City", 2000)

vehicle.display()
vehicle.rent()

print("Rental Charges:", vehicle.rental_charges(5))

vehicle.return_vehicle()
vehicle.display()


# Q11. ShoppingCart with constructor and destructor

class ShoppingCart:
    def __init__(self, customer_name, cart_id):
        self.customer_name = customer_name
        self.cart_id = cart_id
        self.products = []

    def add_product(self, name, price):
        self.products.append([name, price])
        print(name, "added to cart")

    def remove_product(self, name):
        for product in self.products:
            if product[0] == name:
                self.products.remove(product)
                print(name, "removed from cart")
                return

        print("Product not found")

    def total_bill(self):
        total = 0

        for product in self.products:
            total += product[1]

        return total

    def __del__(self):
        print("Shopping cart destroyed")


cart = ShoppingCart("Rahul", 101)

cart.add_product("Laptop", 50000)
cart.add_product("Mouse", 1000)
cart.add_product("Keyboard", 2000)

cart.remove_product("Mouse")

print("Total Bill:", cart.total_bill())

del cart


# Q12. FoodOrder with constructor, tax and destructor

class FoodOrder:
    def __init__(
        self,
        order_id,
        customer_name,
        food_item,
        quantity,
        price
    ):
        self.order_id = order_id
        self.customer_name = customer_name
        self.food_item = food_item
        self.quantity = quantity
        self.price = price

    def total_bill(self):
        subtotal = self.quantity * self.price
        tax = subtotal * 0.05
        return subtotal + tax

    def display(self):
        print("Order ID:", self.order_id)
        print("Customer:", self.customer_name)
        print("Food Item:", self.food_item)
        print("Quantity:", self.quantity)
        print("Price:", self.price)
        print("Total Bill:", self.total_bill())

    def __del__(self):
        print("Order completed")


order = FoodOrder(
    101,
    "Priya",
    "Pizza",
    2,
    300
)

order.display()

del order


# Q13. StudentResult with constructor and destructor

class StudentResult:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def total(self):
        return sum(self.marks)

    def percentage(self):
        return self.total() / 5

    def grade(self):
        percentage = self.percentage()

        if percentage >= 90:
            return "A"
        elif percentage >= 75:
            return "B"
        elif percentage >= 60:
            return "C"
        elif percentage >= 50:
            return "D"
        else:
            return "F"

    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)
        print("Total:", self.total())
        print("Percentage:", self.percentage())
        print("Grade:", self.grade())

    def __del__(self):
        print("StudentResult object destroyed")


result = StudentResult(
    "Amit",
    [85, 90, 78, 88, 92]
)

result.display()

del result
