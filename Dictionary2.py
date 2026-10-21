# 11. Find the student who has scored the highest marks

students = {
    "Rahul": 85,
    "Amit": 75,
    "Priya": 95,
    "Neha": 80
}

highest_student = max(students, key=students.get)
print("Student with highest marks:", highest_student)
print("Marks:", students[highest_student])


# 12. Find the student who has scored the lowest marks

students = {
    "Rahul": 85,
    "Amit": 65,
    "Priya": 95,
    "Neha": 70
}

lowest_student = min(students, key=students.get)

print("Student with lowest marks:", lowest_student)
print("Marks:", students[lowest_student])


# 13. Calculate the average marks of all students

students = {
    "Rahul": 85,
    "Amit": 75,
    "Priya": 95,
    "Neha": 80
}

total = sum(students.values())
average = total / len(students)

print("Average marks:", average)


# 14. Accept a string and create a dictionary containing each character and its frequency

text = input("Enter a string: ")

frequency = {}

for char in text:
    frequency[char] = frequency.get(char, 0) + 1

print("Character frequency:")
print(frequency)


# 15. Accept a sentence and create a dictionary containing each word and its frequency

sentence = input("Enter a sentence: ")

words = sentence.split()
frequency = {}

for word in words:
    frequency[word] = frequency.get(word, 0) + 1

print("Word frequency:")
print(frequency)


# 16. Create two dictionaries and merge them into a single dictionary

dict1 = {
    "a": 10,
    "b": 20,
    "c": 30
}

dict2 = {
    "d": 40,
    "e": 50,
    "f": 60
}

merged = dict1.copy()
merged.update(dict2)

print("Merged dictionary:")
print(merged)


# 17. Given two dictionaries, find the keys that are common to both dictionaries

dict1 = {
    "a": 10,
    "b": 20,
    "c": 30,
    "d": 40
}

dict2 = {
    "b": 50,
    "c": 60,
    "e": 70
}

common_keys = dict1.keys() & dict2.keys()

print("Common keys:")
print(common_keys)


# 18. Given two dictionaries, identify the values that are common to both dictionaries

dict1 = {
    "a": 10,
    "b": 20,
    "c": 30
}

dict2 = {
    "x": 20,
    "y": 30,
    "z": 40
}

common_values = set(dict1.values()) & set(dict2.values())

print("Common values:")
print(common_values)


# 19. Create a dictionary containing duplicate values and remove duplicate values

data = {
    "a": 10,
    "b": 20,
    "c": 10,
    "d": 30,
    "e": 20
}

unique_data = {}
seen = set()

for key, value in data.items():
    if value not in seen:
        unique_data[key] = value
        seen.add(value)

print("Original dictionary:")
print(data)

print("Dictionary after removing duplicate values:")
print(unique_data)


# 20. Create a dictionary and display its elements in ascending order of keys

data = {
    5: "Apple",
    2: "Banana",
    4: "Mango",
    1: "Orange",
    3: "Grapes"
}

sorted_data = dict(sorted(data.items()))

print("Dictionary in ascending order of keys:")

for key, value in sorted_data.items():
    print(key, ":", value)