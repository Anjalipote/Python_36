Sure — here are the first 10 Lambda Function questions in one Python code block, with comments only at the top of each program.

# 1. Lambda function to calculate the square of a number

square = lambda x: x * x

n = int(input("Enter a number: "))
print("Square =", square(n))


# 2. Lambda function to calculate the cube of a number

cube = lambda x: x * x * x

n = int(input("Enter a number: "))
print("Cube =", cube(n))


# 3. Lambda function to check whether a number is even

is_even = lambda x: x % 2 == 0

n = int(input("Enter a number: "))
print(is_even(n))


# 4. Lambda function to find the maximum of two numbers

maximum = lambda a, b: a if a > b else b

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Maximum =", maximum(a, b))


# 5. Lambda function to calculate simple interest

simple_interest = lambda p, r, t: (p * r * t) / 100

p = float(input("Enter principal: "))
r = float(input("Enter rate: "))
t = float(input("Enter time: "))

print("Simple Interest =", simple_interest(p, r, t))


# 6. Use map() and lambda to find squares of numbers

numbers = list(map(int, input("Enter numbers: ").split()))

squares = list(map(lambda x: x * x, numbers))

print("Squares =", squares)


# 7. Use map() and lambda to find cubes of numbers

numbers = list(map(int, input("Enter numbers: ").split()))

cubes = list(map(lambda x: x * x * x, numbers))

print("Cubes =", cubes)


# 8. Use map() and lambda to add corresponding elements of two lists

list1 = list(map(int, input("Enter first list: ").split()))
list2 = list(map(int, input("Enter second list: ").split()))

result = list(map(lambda x, y: x + y, list1, list2))

print("Sum of corresponding elements =", result)


# 9. Use filter() and lambda to extract even numbers

numbers = list(map(int, input("Enter numbers: ").split()))
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers =", even_numbers)


# 10. Use filter() and lambda to find prime numbers

def is_prime(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


numbers = list(map(int, input("Enter numbers: ").split()))
prime_numbers = list(filter(lambda x: is_prime(x), numbers))
print("Prime numbers =", prime_numbers)