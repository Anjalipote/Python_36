# 31. Create a dictionary where the key is word length and value is a list of words having that length

words = ["cat", "dog", "apple", "banana", "bat", "orange"]

result = {}

for word in words:
    length = len(word)

    if length not in result:
        result[length] = []

    result[length].append(word)

print("Words grouped by length:")
print(result)


# 32. Find two numbers whose sum is equal to the target using a dictionary

numbers = [2, 7, 11, 15, 3, 6]
target = int(input("Enter target value: "))

seen = {}

for num in numbers:
    complement = target - num

    if complement in seen:
        print("Two numbers are:", complement, "and", num)
        break

    seen[num] = True
else:
    print("No two numbers found")


# 33. Find the first character that occurs only once

text = input("Enter a string: ")

frequency = {}

for char in text:
    frequency[char] = frequency.get(char, 0) + 1

for char in text:
    if frequency[char] == 1:
        print("First non-repeating character:", char)
        break
else:
    print("No unique character found")


# 34. Find the first character that occurs more than once

text = input("Enter a string: ")

frequency = {}

for char in text:
    frequency[char] = frequency.get(char, 0) + 1

for char in text:
    if frequency[char] > 1:
        print("First repeating character:", char)
        break
else:
    print("No repeating character found")


# 35. Accept a paragraph and create a dictionary where key = word length and value = number of words having that length

paragraph = input("Enter a paragraph: ")

words = paragraph.split()
length_count = {}

for word in words:
    # Remove common punctuation marks
    word = word.strip(".,!?;:")

    length = len(word)

    if length > 0:
        length_count[length] = length_count.get(length, 0) + 1

print("Word length frequency:")

for length, count in sorted(length_count.items()):
    print(length, ":", count)