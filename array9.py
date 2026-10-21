# 8. fromlist() - Add elements from a list

import array

numbers = array.array('i', [10, 20])

numbers.fromlist([30, 40, 50])

print("Array after fromlist:", numbers.tolist())
