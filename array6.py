# 5. extend() - Add multiple elements to the array

import array

numbers = array.array('i', [10, 20, 30])

numbers.extend([40, 50, 60])

print("Array after extend:", numbers.tolist())
