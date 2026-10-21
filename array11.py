# 10. index() - Find the index of an element

import array

numbers = array.array('i', [10, 20, 30, 40])

position = numbers.index(30)

print("Array:", numbers.tolist())
print("Index of 30:", position)
