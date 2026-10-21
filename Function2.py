# 11. Reverse a string

def reverse_string(text):
    return text[::-1]

text = input("Enter a string: ")
print("Reverse =", reverse_string(text))


# 12. Check whether a string or number is a palindrome

def is_palindrome(value):
    value = str(value)
    return value == value[::-1]

value = input("Enter a string or number: ")

if is_palindrome(value):
    print("Palindrome")
else:
    print("Not Palindrome")


# 13. Calculate the average of a list of numbers

def average(numbers):
    total = 0

    for num in numbers:
        total = total + num

    return total / len(numbers)

numbers = list(map(int, input("Enter numbers: ").split()))

print("Average =", average(numbers))


# 14. Count occurrences of an element in a list

def count_element(numbers, element):
    count = 0

    for num in numbers:
        if num == element:
            count = count + 1

    return count

numbers = list(map(int, input("Enter numbers: ").split()))
element = int(input("Enter element to search: "))

print("Occurrences =", count_element(numbers, element))


# 15. Remove duplicate elements from a list

def unique_elements(numbers):
    unique = []

    for num in numbers:
        if num not in unique:
            unique.append(num)

    return unique

numbers = list(map(int, input("Enter numbers: ").split()))
print("Unique elements =", unique_elements(numbers))


# 16. Find the second-largest number in a list

def second_largest(numbers):
    largest = numbers[0]
    second = None

    for num in numbers:
        if num > largest:
            second = largest
            largest = num
        elif num != largest and (second is None or num > second):
            second = num

    return second

numbers = list(map(int, input("Enter numbers: ").split()))
print("Second largest =", second_largest(numbers))


# 17. Generate the first n Fibonacci numbers

def fibonacci(n):
    a = 0
    b = 1
    result = []

    for i in range(n):
        result.append(a)
        a, b = b, a + b
    return result

n = int(input("Enter n: "))
print("Fibonacci numbers =", fibonacci(n))


# 18. Calculate percentage and grade

def percentage_grade(m1, m2, m3, m4, m5):
    total = m1 + m2 + m3 + m4 + m5
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

    return percentage, grade

marks = []

for i in range(5):
    mark = float(input("Enter marks: "))
    marks.append(mark)

percentage, grade = percentage_grade(
    marks[0], marks[1], marks[2], marks[3], marks[4]
)

print("Percentage =", percentage)
print("Grade =", grade)


# 19. Calculate electricity bill according to slabs

def electricity_bill(units):
    if units <= 100:
        bill = units * 5
    elif units <= 200:
        bill = (100 * 5) + ((units - 100) * 7)
    else:
        bill = (100 * 5) + (100 * 7) + ((units - 200) * 10)

    return bill

units = float(input("Enter units consumed: "))
print("Electricity Bill =", electricity_bill(units))


# 20. Calculate gross salary using HRA and DA

def gross_salary(basic):
    if basic <= 10000:
        hra = basic * 0.20
        da = basic * 0.80
    elif basic <= 20000:
        hra = basic * 0.25
        da = basic * 0.90
    else:
        hra = basic * 0.30
        da = basic * 0.95

    return basic + hra + da
basic = float(input("Enter basic salary: "))
print("Gross Salary =", gross_salary(basic))
