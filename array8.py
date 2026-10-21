# 7. fromfile() - Read elements from a binary file

import array

numbers = array.array('i', [10, 20, 30, 40])

with open("numbers.bin", "wb") as file:
    numbers.tofile(file)

new_array = array.array('i')

with open("numbers.bin", "rb") as file:
    new_array.fromfile(file, 4)

print("Array read from file:", new_array.tolist())
