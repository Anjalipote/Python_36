# 6. frombytes() - Add elements from bytes

import array

numbers = array.array('i', [10, 20, 30])

data = array.array('i', [40, 50]).tobytes()

numbers.frombytes(data)

print("Array after frombytes:", numbers.tolist())
