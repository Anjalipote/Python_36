# 11. insert() - Insert an element at a specified position

import array

numbers = array.array('i', [10, 20, 40, 50])

numbers.insert(2, 30)

print("Array after insert:", numbers.tolist())
