# 21. Create two sets representing technical skills of two employees

employee1 = {"Python", "Java", "SQL", "Git"}
employee2 = {"Python", "C++", "SQL", "Docker"}

common_skills = employee1 & employee2
unique_employee1 = employee1 - employee2
unique_employee2 = employee2 - employee1
all_skills = employee1 | employee2

print("Common skills:", common_skills)
print("Skills unique to Employee 1:", unique_employee1)
print("Skills unique to Employee 2:", unique_employee2)
print("All available skills:", all_skills)


# 22. Create sets of available books and requested books

available_books = {
    "Python Programming",
    "Data Structures",
    "Database Management",
    "Computer Networks"
}

requested_books = {
    "Python Programming",
    "Java Programming",
    "Database Management",
    "Operating Systems"
}

available_requested = available_books & requested_books

print("Requested books that are available:")
print(available_requested)


# 23. Store visitor IDs from two different days

day1 = {101, 102, 103, 104, 105}
day2 = {103, 104, 105, 106, 107}

unique_visitors = day1 | day2
returning_visitors = day1 & day2
only_first_day = day1 - day2
only_second_day = day2 - day1

print("Unique visitors:", unique_visitors)
print("Returning visitors:", returning_visitors)
print("Visitors only on first day:", only_first_day)
print("Visitors only on second day:", only_second_day)


# 24. Create sets representing products belonging to different categories

category1 = {"Laptop", "Mobile", "Tablet", "Headphones", "Camera"}
category2 = {"Mobile", "Camera", "Printer", "Headphones", "Speaker"}

common_products = category1 & category2

print("Products belonging to both categories:")
print(common_products)


# 25. Represent the friends of two users using sets

user1 = {"Rahul", "Amit", "Priya", "Neha"}
user2 = {"Priya", "Neha", "Rohan", "Kiran"}

mutual_friends = user1 & user2
unique_user1 = user1 - user2
unique_user2 = user2 - user1
all_friends = user1 | user2

print("Mutual friends:", mutual_friends)
print("Friends unique to User 1:", unique_user1)
print("Friends unique to User 2:", unique_user2)
print("Total unique friends:", len(all_friends))
