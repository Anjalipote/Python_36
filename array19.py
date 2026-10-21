# 18. tounicode() - Convert a Unicode array into a string

import array

characters = array.array('u', ['P', 'y', 't', 'h', 'o', 'n'])

text = characters.tounicode()

print("Array:", characters.tolist())
print("String:", text)
