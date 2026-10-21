
# 13. remove() - Remove the first occurrence of an element

import array

numbers = array.array('i', [10, 20, 30, 20, 40])

numbers.remove(20)

print("Array after remove:", numbers.tolist())
