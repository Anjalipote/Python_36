# 17. tolist() - Convert the array into a list

import array

numbers = array.array('i', [10, 20, 30, 40])

my_list = numbers.tolist()

print("Array:", numbers.tolist())
print("List:", my_list)
