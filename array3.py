# 3. byteswap() - Swap the byte order of each element

import array

numbers = array.array('i', [1, 2, 3, 4])

print("Original array:", numbers.tolist())

numbers.byteswap()

print("Array after byteswap:", numbers.tolist())
