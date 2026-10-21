# 1. append() - Add an element to the array

import array

numbers = array.array('i', [10, 20, 30])

numbers.append(40)

print("Array after append:", numbers.tolist())
