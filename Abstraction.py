# Q1. Abstract Shape -> Circle, Rectangle, Triangle

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    @abstractmethod
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


c = Circle(5)
r = Rectangle(10, 5)
t = Triangle(8, 6)

print("Circle Area:", c.area())
print("Rectangle Area:", r.area())
print("Triangle Area:", t.area())


# Q2. Abstract Vehicle -> Car, Bike, Bus

from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Car(Vehicle):
    def start(self):
        print("Car starts with a key")

    def stop(self):
        print("Car stops using brakes")


class Bike(Vehicle):
    def start(self):
        print("Bike starts with self-start")

    def stop(self):
        print("Bike stops using brakes")


class Bus(Vehicle):
    def start(self):
        print("Bus starts with ignition")

    def stop(self):
        print("Bus stops at the bus stop")


car = Car()
bike = Bike()
bus = Bus()

car.start()
car.stop()

bike.start()
bike.stop()

bus.start()
bus.stop()


# Q3. Abstract BankAccount -> SavingsAccount, CurrentAccount

from abc import ABC, abstractmethod


class BankAccount(ABC):
    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass


class SavingsAccount(BankAccount):
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient balance")


class CurrentAccount(BankAccount):
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient balance")


s = SavingsAccount(10000)
s.deposit(2000)
s.withdraw(3000)
print("Savings Balance:", s.balance)

c = CurrentAccount(20000)
c.deposit(5000)
c.withdraw(7000)
print("Current Balance:", c.balance)


# Q4. Abstract FoodOrder -> RestaurantOrder, HomeDeliveryOrder

from abc import ABC, abstractmethod


class FoodOrder(ABC):
    @abstractmethod
    def calculate_bill(self):
        pass

    @abstractmethod
    def delivery_charge(self):
        pass


class RestaurantOrder(FoodOrder):
    def __init__(self, food_price):
        self.food_price = food_price

    def calculate_bill(self):
        return self.food_price

    def delivery_charge(self):
        return 0


class HomeDeliveryOrder(FoodOrder):
    def __init__(self, food_price):
        self.food_price = food_price

    def calculate_bill(self):
        return self.food_price

    def delivery_charge(self):
        return 50


restaurant = RestaurantOrder(500)
home = HomeDeliveryOrder(500)

print("Restaurant Bill:", restaurant.calculate_bill())
print("Restaurant Delivery:", restaurant.delivery_charge())

print("Home Delivery Bill:", home.calculate_bill())
print("Home Delivery Charge:", home.delivery_charge())


# Q5. Abstract Patient -> InPatient, OutPatient, EmergencyPatient

from abc import ABC, abstractmethod


class Patient(ABC):
    @abstractmethod
    def calculate_bill(self):
        pass

    @abstractmethod
    def treatment(self):
        pass


class InPatient(Patient):
    def calculate_bill(self):
        return 5000

    def treatment(self):
        print("In-patient receives hospital treatment")


class OutPatient(Patient):
    def calculate_bill(self):
        return 1000

    def treatment(self):
        print("Out-patient receives consultation")


class EmergencyPatient(Patient):
    def calculate_bill(self):
        return 10000

    def treatment(self):
        print("Emergency patient receives immediate treatment")


ip = InPatient()
op = OutPatient()
ep = EmergencyPatient()

print("InPatient Bill:", ip.calculate_bill())
ip.treatment()

print("OutPatient Bill:", op.calculate_bill())
op.treatment()

print("Emergency Bill:", ep.calculate_bill())
ep.treatment()


# Q6. Abstract Transport -> Bus, Train, Taxi, Flight

from abc import ABC, abstractmethod


class Transport(ABC):
    @abstractmethod
    def calculate_fare(self, distance):
        pass


class Bus(Transport):
    def calculate_fare(self, distance):
        return distance * 2


class Train(Transport):
    def calculate_fare(self, distance):
        return distance * 3


class Taxi(Transport):
    def calculate_fare(self, distance):
        return distance * 10


class Flight(Transport):
    def calculate_fare(self, distance):
        return distance * 15


distance = 100

print("Bus Fare:", Bus().calculate_fare(distance))
print("Train Fare:", Train().calculate_fare(distance))
print("Taxi Fare:", Taxi().calculate_fare(distance))
print("Flight Fare:", Flight().calculate_fare(distance))


# Q7. Abstract Question -> MCQ, TrueFalse, Descriptive

from abc import ABC, abstractmethod


class Question(ABC):
    @abstractmethod
    def evaluate_answer(self, answer):
        pass


class MCQQuestion(Question):
    def __init__(self, correct_answer):
        self.correct_answer = correct_answer

    def evaluate_answer(self, answer):
        if answer == self.correct_answer:
            return "Correct"
        return "Wrong"


class TrueFalseQuestion(Question):
    def __init__(self, correct_answer):
        self.correct_answer = correct_answer

    def evaluate_answer(self, answer):
        if answer == self.correct_answer:
            return "Correct"
        return "Wrong"


class DescriptiveQuestion(Question):
    def evaluate_answer(self, answer):
        if len(answer) > 20:
            return "Answer accepted for evaluation"
        return "Answer too short"


mcq = MCQQuestion("B")
tf = TrueFalseQuestion(True)
desc = DescriptiveQuestion()

print(mcq.evaluate_answer("B"))
print(tf.evaluate_answer(True))
print(desc.evaluate_answer(
    "Python is an object oriented programming language."
))


# Q8. Abstract Authentication -> Password, OTP, Biometric

from abc import ABC, abstractmethod


class Authentication(ABC):
    @abstractmethod
    def authenticate(self):
        pass


class PasswordAuthentication(Authentication):
    def authenticate(self):
        print("Authenticated using password")


class OTPAuthentication(Authentication):
    def authenticate(self):
        print("Authenticated using OTP")


class BiometricAuthentication(Authentication):
    def authenticate(self):
        print("Authenticated using biometric")


p = PasswordAuthentication()
o = OTPAuthentication()
b = BiometricAuthentication()

p.authenticate()
o.authenticate()
b.authenticate()


# Q9. Abstract CloudStorage -> Storage Services

from abc import ABC, abstractmethod


class CloudStorage(ABC):
    @abstractmethod
    def upload_file(self, filename):
        pass

    @abstractmethod
    def download_file(self, filename):
        pass

    @abstractmethod
    def delete_file(self, filename):
        pass


class GoogleDrive(CloudStorage):
    def upload_file(self, filename):
        print(filename, "uploaded to Google Drive")

    def download_file(self, filename):
        print(filename, "downloaded from Google Drive")

    def delete_file(self, filename):
        print(filename, "deleted from Google Drive")


class Dropbox(CloudStorage):
    def upload_file(self, filename):
        print(filename, "uploaded to Dropbox")

    def download_file(self, filename):
        print(filename, "downloaded from Dropbox")

    def delete_file(self, filename):
        print(filename, "deleted from Dropbox")


g = GoogleDrive()
d = Dropbox()

g.upload_file("document.pdf")
g.download_file("document.pdf")
g.delete_file("document.pdf")

d.upload_file("photo.jpg")
d.download_file("photo.jpg")
d.delete_file("photo.jpg")


# Q10. Abstract Appointment -> General, Specialist, Emergency

from abc import ABC, abstractmethod


class Appointment(ABC):
    @abstractmethod
    def book_appointment(self):
        pass

    @abstractmethod
    def calculate_fee(self):
        pass


class GeneralAppointment(Appointment):
    def book_appointment(self):
        print("General appointment booked")

    def calculate_fee(self):
        return 500


class SpecialistAppointment(Appointment):
    def book_appointment(self):
        print("Specialist appointment booked")

    def calculate_fee(self):
        return 1000


class EmergencyAppointment(Appointment):
    def book_appointment(self):
        print("Emergency appointment booked")

    def calculate_fee(self):
        return 2000


general = GeneralAppointment()
specialist = SpecialistAppointment()
emergency = EmergencyAppointment()

general.book_appointment()
print("Fee:", general.calculate_fee())

specialist.book_appointment()
print("Fee:", specialist.calculate_fee())

emergency.book_appointment()
print("Fee:", emergency.calculate_fee())
