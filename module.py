# Task 1: Calculator module creation and usage
with open("calculator.py", "w") as f:
    f.write("def add(a, b): return a + b\n")
    f.write("def sub(a, b): return a - b\n")
    f.write("def mul(a, b): return a * b\n")
    f.write("def div(a, b): return a / b if b != 0 else 'Division by zero error'\n")

import calculator
print("--- Task 1: Calculator Module ---")
print("Addition (10 + 5):", calculator.add(10, 5))
print("Division (10 / 2):", calculator.div(10, 2))


# Task 2: Student module creation (total marks, percentage, grade) and usage
with open("student_mod.py", "w") as f:
    f.write("def calculate_total(marks): return sum(marks)\n")
    f.write("def calculate_percentage(total, max_marks): return (total / max_marks) * 100\n")
    f.write("def calculate_grade(percentage):\n")
    f.write("    if percentage >= 90: return 'A'\n")
    f.write("    elif percentage >= 75: return 'B'\n")
    f.write("    elif percentage >= 50: return 'C'\n")
    f.write("    else: return 'Fail'\n")

import student_mod
print("\n--- Task 2: Student Module ---")
marks_list = [85, 90, 78, 92, 88]
total = student_mod.calculate_total(marks_list)
percentage = student_mod.calculate_percentage(total, 500)
grade = student_mod.calculate_grade(percentage)
print(f"Total: {total}, Percentage: {percentage:.2f}%, Grade: {grade}")


# Task 3: Number utils module (prime, palindrome, Armstrong, perfect) and import
with open("number_utils.py", "w") as f:
    f.write("def is_prime(n):\n    if n <= 1: return False\n    for i in range(2, int(n**0.5)+1):\n        if n % i == 0: return False\n    return True\n")
    f.write("def is_palindrome(n):\n    return str(n) == str(n)[::-1]\n")
    f.write("def is_armstrong(n):\n    s = str(n)\n    return n == sum(int(char)**len(s) for char in s)\n")
    f.write("def is_perfect(n):\n    return n == sum(i for i in range(1, n) if n % i == 0)\n")

from number_utils import is_prime, is_palindrome, is_armstrong, is_perfect
print("\n--- Task 3: Number Utils Module ---")
num = 153
print(f"Number: {num}")
print(f"Is Prime: {is_prime(num)}")
print(f"Is Palindrome: {is_palindrome(num)}")
print(f"Is Armstrong: {is_armstrong(num)}")
print(f"Is Perfect: {is_perfect(num)}")


# Task 4: String utils module (vowels, reverse, palindrome, words, remove spaces)
with open("string_utils.py", "w") as f:
    f.write("def count_vowels(s): return sum(1 for c in s.lower() if c in 'aeiou')\n")
    f.write("def reverse_string(s): return s[::-1]\n")
    f.write("def check_palindrome(s): s_clean = s.replace(' ', '').lower(); return s_clean == s_clean[::-1]\n")
    f.write("def count_words(s): return len(s.split())\n")
    f.write("def remove_spaces(s): return ''.join(s.split())\n")

import string_utils
print("\n--- Task 4: String Utils Module ---")
text_sample = "Madam In Eden Im Adam"
print(f"Original: '{text_sample}'")
print(f"Vowels: {string_utils.count_vowels(text_sample)}")
print(f"Reversed: '{string_utils.reverse_string(text_sample)}'")
print(f"Is Palindrome: {string_utils.check_palindrome(text_sample)}")
print(f"Word Count: {string_utils.count_words(text_sample)}")
print(f"Without Spaces: '{string_utils.remove_spaces(text_sample)}'")


# Task 5: Employee salary module (gross salary, deductions, net salary)
with open("salary_utils.py", "w") as f:
    f.write("def calculate_gross(basic, hra, da): return basic + hra + da\n")
    f.write("def calculate_deductions(tax, pf): return tax + pf\n")
    f.write("def calculate_net(gross, deductions): return gross - deductions\n")

import salary_utils
print("\n--- Task 5: Employee Salary Module ---")
basic, hra, da, tax, pf = 40000, 10000, 5000, 3000, 2000
gross = salary_utils.calculate_gross(basic, hra, da)
deductions = salary_utils.calculate_deductions(tax, pf)
net = salary_utils.calculate_net(gross, deductions)
print(f"Gross Salary: {gross}, Deductions: {deductions}, Net Salary: {net}")