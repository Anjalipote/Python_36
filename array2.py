# 2. buffer_info() - Display memory address and number of elements

import array

numbers = array.array('i', [10, 20, 30, 40])

print("Array:", numbers.tolist())
print("Buffer information:", numbers.buffer_info())
