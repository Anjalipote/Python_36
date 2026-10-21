# 11. Find elements present in the first set but not the second,
# and elements present in the second set but not the first

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

first_only = set1 - set2
second_only = set2 - set1

print("Elements only in first set:", first_only)
print("Elements only in second set:", second_only)


# 12. Find elements present in either set but not in both

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

result = set1.symmetric_difference(set2)

print("Elements in either set but not both:", result)


# 13. Check whether the first set is a subset of the second set

set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}

if set1.issubset(set2):
    print("First set is a subset of the second set")
else:
    print("First set is not a subset of the second set")


# 14. Check whether the first set is a superset of the second set

set1 = {1, 2, 3, 4, 5}
set2 = {1, 2, 3}

if set1.issuperset(set2):
    print("First set is a superset of the second set")
else:
    print("First set is not a superset of the second set")


# 15. Determine whether two sets have no elements in common

set1 = {1, 2, 3}
set2 = {4, 5, 6}

if set1.isdisjoint(set2):
    print("The two sets have no elements in common")
else:
    print("The two sets have common elements")


# 16. Check whether two sets are equal

set1 = {1, 2, 3, 4}
set2 = {4, 3, 2, 1}

if set1 == set2:
    print("Both sets are equal")
else:
    print("Both sets are not equal")


# 17. Find the subjects studied by both students

student1 = {"Python", "Java", "Maths", "Database"}
student2 = {"Python", "C++", "Maths", "Networks"}

common_subjects = student1 & student2

print("Subjects studied by both students:", common_subjects)


# 18. Accept a sentence and display all unique words

sentence = input("Enter a sentence: ")

words = sentence.split()
unique_words = set(words)

print("Unique words:")

for word in unique_words:
    print(word)


# 19. Find students present in both sessions,
# only in morning, only in afternoon, and at least one session

morning = {"Rahul", "Amit", "Priya", "Neha"}
afternoon = {"Priya", "Neha", "Rohan", "Kiran"}

both = morning & afternoon
only_morning = morning - afternoon
only_afternoon = afternoon - morning
at_least_one = morning | afternoon

print("Students in both sessions:", both)
print("Students only in morning:", only_morning)
print("Students only in afternoon:", only_afternoon)
print("Students in at least one session:", at_least_one)


# 20. Find students enrolled in both Python and Java
# and students enrolled in only one course

python_students = {"Rahul", "Amit", "Priya", "Neha"}
java_students = {"Priya", "Neha", "Rohan", "Kiran"}

both_courses = python_students & java_students
only_one_course = python_students ^ java_students

print("Students in both courses:", both_courses)
print("Students in only one course:", only_one_course)