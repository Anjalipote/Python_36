# 12. pop() - Remove and return an element

import array

numbers = array.array('i', [10, 20, 30, 40])

removed = numbers.pop()

print("Removed element:", removed)
print("Array after pop:", numbers.tolist())
