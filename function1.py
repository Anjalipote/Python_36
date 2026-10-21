# 1. Find the factorial of a number

def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact

n = int(input("Enter a number: "))
print("Factorial =", factorial(n))

# 2. Check whether a number is even or odd

def check_even_odd(n):
    if n % 2 == 0:
        return "Even"
    return "Odd"

n = int(input("Enter a number: "))
print(check_even_odd(n))


# 3. Find the greater of two numbers

def greater(a, b):
    if a > b:
        return a
    return b

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Greater number =", greater(a, b))


# 4. Calculate simple interest

def simple_interest(p, r, t):
    return (p * r * t) / 100

p = float(input("Enter principal: "))
r = float(input("Enter rate: "))
t = float(input("Enter time: "))

print("Simple Interest =", simple_interest(p, r, t))


# 5. Check whether a number is prime

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False

    return True

n = int(input("Enter a number: "))

if is_prime(n):
    print("Prime")
else:
    print("Not Prime")


# 6. Calculate the area of a circle

def area_circle(radius):
    return 3.14 * radius * radius

radius = float(input("Enter radius: "))
print("Area of circle =", area_circle(radius))


# 7. Calculate the sum of first n natural numbers

def natural_sum(n):
    total = 0
    for i in range(1, n + 1):
        total = total + i

    return total

n = int(input("Enter n: "))
print("Sum =", natural_sum(n))


# 8. Calculate the power of a number

def power(base, exponent):
    result = 1
    for i in range(exponent):
        result = result * base

    return result

base = int(input("Enter base: "))
exponent = int(input("Enter exponent: "))
print("Power =", power(base, exponent))


# 9. Find the largest element without using max()

def largest(numbers):
    largest_num = numbers[0]
    for num in numbers:
        if num > largest_num:
            largest_num = num

    return largest_num

numbers = list(map(int, input("Enter numbers: ").split()))
print("Largest =", largest(numbers))


# 10. Count the number of vowels in a string

def count_vowels(text):
    count = 0
    for ch in text.lower():
        if ch in "aeiou":
            count = count + 1

    return count

text = input("Enter a string: ")
print("Number of vowels =", count_vowels(text))