# 15. tobytes() - Convert the array into bytes

import array

numbers = array.array('i', [10, 20, 30])

data = numbers.tobytes()

print("Array:", numbers.tolist())
print("Bytes:", data)
