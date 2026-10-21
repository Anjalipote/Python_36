# Q1. Shape -> Circle, Rectangle, Triangle

import math


class Shape:
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


shapes = [
    Circle(5),
    Rectangle(10, 5),
    Triangle(8, 6)
]

for shape in shapes:
    print("Area:", shape.area())


# Q2. Employee -> Manager, Developer, Tester

class Employee:
    def calculate_salary(self):
        pass


class Manager(Employee):
    def calculate_salary(self):
        return 50000 + 15000


class Developer(Employee):
    def calculate_salary(self):
        return 50000 + 10000


class Tester(Employee):
    def calculate_salary(self):
        return 50000 + 7500


employees = [
    Manager(),
    Developer(),
    Tester()
]

for employee in employees:
    print("Salary:", employee.calculate_salary())


# Q3. Vehicle -> Car, Bike, Bus

class Vehicle:
    def start(self):
        pass


class Car(Vehicle):
    def start(self):
        print("Car starts with a key")


class Bike(Vehicle):
    def start(self):
        print("Bike starts with self-start")


class Bus(Vehicle):
    def start(self):
        print("Bus starts with ignition")


vehicles = [Car(), Bike(), Bus()]

for vehicle in vehicles:
    vehicle.start()


# Q4. Animal -> Dog, Cat, Cow, Lion

class Animal:
    def sound(self):
        pass


class Dog(Animal):
    def sound(self):
        print("Dog says Woof")


class Cat(Animal):
    def sound(self):
        print("Cat says Meow")


class Cow(Animal):
    def sound(self):
        print("Cow says Moo")


class Lion(Animal):
    def sound(self):
        print("Lion says Roar")


animals = [Dog(), Cat(), Cow(), Lion()]

for animal in animals:
    animal.sound()


# Q5. Notification -> Email, SMS, Push

class Notification:
    def send(self):
        pass


class EmailNotification(Notification):
    def send(self):
        print("Sending Email Notification")


class SMSNotification(Notification):
    def send(self):
        print("Sending SMS Notification")


class PushNotification(Notification):
    def send(self):
        print("Sending Push Notification")


notifications = [
    EmailNotification(),
    SMSNotification(),
    PushNotification()
]

for notification in notifications:
    notification.send()


# Q6. Student -> Engineering, Medical, Management

class Student:
    def calculate_grade(self):
        pass


class EngineeringStudent(Student):
    def calculate_grade(self):
        print("Engineering Student Grade: A")


class MedicalStudent(Student):
    def calculate_grade(self):
        print("Medical Student Grade: B")


class ManagementStudent(Student):
    def calculate_grade(self):
        print("Management Student Grade: A")


students = [
    EngineeringStudent(),
    MedicalStudent(),
    ManagementStudent()
]

for student in students:
    student.calculate_grade()


# Q7. BankAccount -> Savings, Current, FixedDeposit

class BankAccount:
    def calculate_interest(self, balance):
        pass


class SavingsAccount(BankAccount):
    def calculate_interest(self, balance):
        return balance * 0.05


class CurrentAccount(BankAccount):
    def calculate_interest(self, balance):
        return balance * 0.02


class FixedDepositAccount(BankAccount):
    def calculate_interest(self, balance):
        return balance * 0.08


accounts = [
    SavingsAccount(),
    CurrentAccount(),
    FixedDepositAccount()
]

for account in accounts:
    print("Interest:", account.calculate_interest(100000))


# Q8. Report -> PDF, Excel, HTML

class Report:
    def generate(self):
        pass


class PDFReport(Report):
    def generate(self):
        print("Generating PDF Report")


class ExcelReport(Report):
    def generate(self):
        print("Generating Excel Report")


class HTMLReport(Report):
    def generate(self):
        print("Generating HTML Report")


def generate_report(report):
    report.generate()


reports = [
    PDFReport(),
    ExcelReport(),
    HTMLReport()
]

for report in reports:
    generate_report(report)


# Q9. Distance operator overloading

class Distance:
    def __init__(self, feet, inches):
        self.feet = feet
        self.inches = inches

    def __add__(self, other):
        total_inches = self.inches + other.inches
        total_feet = self.feet + other.feet

        if total_inches >= 12:
            total_feet += total_inches // 12
            total_inches = total_inches % 12

        return Distance(total_feet, total_inches)

    def display(self):
        print(self.feet, "feet", self.inches, "inches")


d1 = Distance(5, 8)
d2 = Distance(4, 7)

d3 = d1 + d2

d3.display()


# Q10. Student comparison using > and <

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __gt__(self, other):
        return self.marks > other.marks

    def __lt__(self, other):
        return self.marks < other.marks


s1 = Student("Rahul", 85)
s2 = Student("Amit", 75)

print("Rahul has greater marks:", s1 > s2)
print("Rahul has lesser marks:", s1 < s2)


# Q11. Product comparison using == and >

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __eq__(self, other):
        return self.price == other.price

    def __gt__(self, other):
        return self.price > other.price


p1 = Product("Laptop", 70000)
p2 = Product("Mobile", 50000)

print("Prices are equal:", p1 == p2)
print("Laptop is more expensive:", p1 > p2)


# Q12. Payment -> UPI, Card, Wallet

class Payment:
    def make_payment(self, amount):
        pass


class UPIPayment(Payment):
    def make_payment(self, amount):
        print("Paid", amount, "using UPI")


class CardPayment(Payment):
    def make_payment(self, amount):
        print("Paid", amount, "using Card")


class WalletPayment(Payment):
    def make_payment(self, amount):
        print("Paid", amount, "using Wallet")


def process_payment(payment, amount):
    payment.make_payment(amount)


payments = [
    UPIPayment(),
    CardPayment(),
    WalletPayment()
]

for payment in payments:
    process_payment(payment, 1000)


# Q13. Person -> Student, Faculty, Administrator

class Person:
    def display_role(self):
        pass


class Student(Person):
    def display_role(self):
        print("Role: Student")


class Faculty(Person):
    def display_role(self):
        print("Role: Faculty")


class Administrator(Person):
    def display_role(self):
        print("Role: Administrator")


people = [
    Student(),
    Faculty(),
    Administrator()
]

for person in people:
    person.display_role()


# Q14. Media -> Audio, Video, Podcast

class Media:
    def play(self):
        pass


class Audio(Media):
    def play(self):
        print("Playing Audio")


class Video(Media):
    def play(self):
        print("Playing Video")


class Podcast(Media):
    def play(self):
        print("Playing Podcast")


media_list = [
    Audio(),
    Video(),
    Podcast()
]

for media in media_list:
    media.play()


# Q15. SmartDevice -> Light, Fan, AC, TV

class SmartDevice:
    def turn_on(self):
        pass

    def turn_off(self):
        pass


class Light(SmartDevice):
    def turn_on(self):
        print("Light turned ON")

    def turn_off(self):
        print("Light turned OFF")


class Fan(SmartDevice):
    def turn_on(self):
        print("Fan turned ON")

    def turn_off(self):
        print("Fan turned OFF")


class AC(SmartDevice):
    def turn_on(self):
        print("AC turned ON")

    def turn_off(self):
        print("AC turned OFF")


class TV(SmartDevice):
    def turn_on(self):
        print("TV turned ON")

    def turn_off(self):
        print("TV turned OFF")


devices = [
    Light(),
    Fan(),
    AC(),
    TV()
]

for device in devices:
    device.turn_on()
    device.turn_off()
