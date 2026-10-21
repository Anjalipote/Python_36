# 1. Create a set containing five integers and display all its elements

numbers = {10, 20, 30, 40, 50}

for number in numbers:
    print(number)


# 2. Create a list containing duplicate values and convert it into a set

numbers = [10, 20, 10, 30, 20, 40, 30, 50]

result = set(numbers)

print("Set:", result)


# 3. Create a set of five fruits and add two new fruits

fruits = {"Apple", "Banana", "Mango", "Orange", "Grapes"}

fruits.add("Pineapple")
fruits.add("Watermelon")

print("Updated set:", fruits)


# 4. Create a set of numbers and remove a specified number

numbers = {10, 20, 30, 40, 50}

num = int(input("Enter number to remove: "))

if num in numbers:
    numbers.remove(num)
    print("Updated set:", numbers)
else:
    print("Number not found")


# 5. Create a set of student names and check whether a student exists

students = {"Rahul", "Amit", "Priya", "Neha", "Rohan"}

name = input("Enter student name: ")

if name in students:
    print("Student exists")
else:
    print("Student does not exist")


# 6. Create a set of cities and find the total number of cities

cities = {"Mumbai", "Pune", "Delhi", "Chennai", "Bangalore"}

print("Cities:", cities)
print("Total number of cities:", len(cities))


# 7. Create a set of programming languages and display each language using a for loop

languages = {"Python", "Java", "C", "C++", "JavaScript"}

for language in languages:
    print(language)


# 8. Create a list containing duplicate numbers and use a set to remove duplicates

numbers = [1, 2, 3, 2, 4, 1, 5, 3, 6, 4]

unique_numbers = set(numbers)

print("Original list:", numbers)
print("After removing duplicates:", unique_numbers)


# 9. Create two sets of integers and find their union

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

union_set = set1.union(set2)

print("Union:", union_set)


# 10. Create two sets and find the elements common to both sets

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

common = set1.intersection(set2)

print("Common elements:", common)