# 16. tofile() - Write array elements to a binary file

import array

numbers = array.array('i', [10, 20, 30, 40])

with open("numbers.bin", "wb") as file:
    numbers.tofile(file)

print("Array:", numbers.tolist())
print("Array successfully written to file.")
