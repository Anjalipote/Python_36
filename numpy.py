# ============================================================
# COMMANDS TO RUN
# ============================================================

# Install NumPy:
# pip install numpy

# Run this Python file:
# python numpy_practical.py


import numpy as np


# ============================================================
# 1. CREATE 1D ARRAY OF 10 INTEGERS
# Display array, size, data type and dimensions
# ============================================================

print("\n===== 1. 1D ARRAY =====")

a = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

print("Array:", a)
print("Size:", a.size)
print("Data type:", a.dtype)
print("Dimensions:", a.ndim)


# ============================================================
# 2. ADDITION, SUBTRACTION, MULTIPLICATION, DIVISION, MODULUS
# ============================================================

print("\n===== 2. ARITHMETIC OPERATIONS =====")

a = np.array([10, 20, 30, 40, 50])
b = np.array([2, 4, 5, 8, 10])

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)


# ============================================================
# 3. MAXIMUM, MINIMUM, SUM AND AVERAGE
# ============================================================

print("\n===== 3. STATISTICAL OPERATIONS =====")

a = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

print("Maximum:", np.max(a))
print("Minimum:", np.min(a))
print("Sum:", np.sum(a))
print("Average:", np.mean(a))


# ============================================================
# 4. BOOLEAN INDEXING - EVEN AND ODD NUMBERS
# ============================================================

print("\n===== 4. EVEN AND ODD NUMBERS =====")

a = np.arange(1, 21)

even = a[a % 2 == 0]
odd = a[a % 2 != 0]

print("Even numbers:", even)
print("Odd numbers:", odd)


# ============================================================
# 5. RESHAPE ARRAY 1 TO 12
# 2x6, 3x4 and 4x3
# ============================================================

print("\n===== 5. RESHAPING =====")

a = np.arange(1, 13)

print("2 x 6 Matrix:")
print(a.reshape(2, 6))

print("3 x 4 Matrix:")
print(a.reshape(3, 4))

print("4 x 3 Matrix:")
print(a.reshape(4, 3))


# ============================================================
# 6. MATRIX ADDITION
# ============================================================

print("\n===== 6. MATRIX ADDITION =====")

a = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

b = np.array([[9, 8, 7],
              [6, 5, 4],
              [3, 2, 1]])

print("Matrix A:")
print(a)

print("Matrix B:")
print(b)

print("Addition:")
print(a + b)


# ============================================================
# 7. MATRIX MULTIPLICATION
# ============================================================

print("\n===== 7. MATRIX MULTIPLICATION =====")

a = np.array([[1, 2],
              [3, 4]])

b = np.array([[5, 6],
              [7, 8]])

result = np.matmul(a, b)

print("Matrix A:")
print(a)

print("Matrix B:")
print(b)

print("Matrix Multiplication:")
print(result)


# ============================================================
# 8. TRANSPOSE OF 3x4 MATRIX
# ============================================================

print("\n===== 8. MATRIX TRANSPOSE =====")

a = np.array([[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12]])

print("Original Matrix:")
print(a)

print("Transpose:")
print(a.T)


# ============================================================
# 9. ACCESS ROWS, COLUMN AND DIAGONAL
# ============================================================

print("\n===== 9. ARRAY INDEXING =====")

a = np.array([[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12],
              [13, 14, 15, 16]])

print("First row:")
print(a[0])

print("Last column:")
print(a[:, -1])

print("Diagonal elements:")
print(np.diag(a))

print("Second and third rows:")
print(a[1:3])


# ============================================================
# 10. SUM OF EACH ROW AND EACH COLUMN
# ============================================================

print("\n===== 10. ROW AND COLUMN SUM =====")

a = np.array([[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12],
              [13, 14, 15, 16]])

print("Sum of each row:")
print(np.sum(a, axis=1))

print("Sum of each column:")
print(np.sum(a, axis=0))


# ============================================================
# 11. ARRAY SLICING
# First 5, Last 5, Alternate and Reverse
# ============================================================

print("\n===== 11. ARRAY SLICING =====")

a = np.arange(1, 21)

print("First 5 elements:")
print(a[:5])

print("Last 5 elements:")
print(a[-5:])

print("Alternate elements:")
print(a[::2])

print("Reverse order:")
print(a[::-1])


# ============================================================
# 12. REPLACE VALUES GREATER THAN 50 WITH 0
# ============================================================

print("\n===== 12. BOOLEAN INDEXING =====")

a = np.array([10, 60, 30, 80, 45, 90, 20, 70, 40, 100])

print("Original array:")
print(a)

a[a > 50] = 0

print("After replacing values greater than 50:")
print(a)


# ============================================================
# 13. ASCENDING AND DESCENDING ORDER
# ============================================================

print("\n===== 13. SORTING =====")

a = np.array([50, 10, 80, 30, 20, 90, 40])

print("Original array:")
print(a)

print("Ascending order:")
print(np.sort(a))

print("Descending order:")
print(np.sort(a)[::-1])


# ============================================================
# 14. UNIQUE ELEMENTS
# ============================================================

print("\n===== 14. UNIQUE ELEMENTS =====")

a = np.array([10, 20, 10, 30, 20, 40, 30, 50])

print("Original array:")
print(a)

print("Unique elements:")
print(np.unique(a))


# ============================================================
# 15. HORIZONTAL AND VERTICAL CONCATENATION
# ============================================================

print("\n===== 15. CONCATENATION =====")

a = np.array([[1, 2],
              [3, 4]])

b = np.array([[5, 6],
              [7, 8]])

print("Horizontal concatenation:")
print(np.hstack((a, b)))

print("Vertical concatenation:")
print(np.vstack((a, b)))


# ============================================================
# 16. MARKS OF 10 STUDENTS
# Highest, Lowest, Average, Median, Standard Deviation
# ============================================================

print("\n===== 16. STUDENT MARKS =====")

marks = np.array([75, 80, 65, 90, 85, 70, 95, 60, 88, 78])

print("Marks:", marks)

print("Highest marks:", np.max(marks))
print("Lowest marks:", np.min(marks))
print("Average marks:", np.mean(marks))
print("Median:", np.median(marks))
print("Standard deviation:", np.std(marks))


# ============================================================
# 17. MARKS OF 20 STUDENTS
# Display students who scored above average
# ============================================================

print("\n===== 17. ABOVE AVERAGE MARKS =====")

marks = np.array([
    65, 78, 85, 90, 55,
    72, 88, 92, 60, 75,
    81, 69, 95, 58, 77,
    84, 70, 89, 63, 80
])

average = np.mean(marks)

print("Marks:")
print(marks)

print("Class average:", average)

print("Students scoring above average:")
print(marks[marks > average])


# ============================================================
# 18. 3D ARRAY OF SHAPE (2,3,4)
# Display dimensions, shape and size
# ============================================================

print("\n===== 18. 3D ARRAY =====")

a = np.arange(1, 25).reshape(2, 3, 4)

print("3D Array:")
print(a)

print("Number of dimensions:", a.ndim)
print("Shape:", a.shape)
print("Size:", a.size)


# ============================================================
# 19. ACCESS ELEMENTS FROM 3D ARRAY
# ============================================================

print("\n===== 19. 3D ARRAY INDEXING =====")

a = np.arange(1, 25).reshape(2, 3, 4)

print("First element:", a[0, 0, 0])
print("Last element:", a[-1, -1, -1])
print("Element at index [0,1,2]:", a[0, 1, 2])
print("Element at index [1,2,3]:", a[1, 2, 3])


# ============================================================
# 20. SUM OF 3D ARRAY
# Sum of all elements, each layer, rows and columns
# ============================================================

print("\n===== 20. 3D ARRAY SUM =====")

a = np.arange(1, 25).reshape(2, 3, 4)

print("Sum of all elements:")
print(np.sum(a))

print("Sum of each layer:")
print(np.sum(a, axis=(1, 2)))

print("Sum along rows:")
print(np.sum(a, axis=2))

print("Sum along columns:")
print(np.sum(a, axis=1))


# ============================================================
# 21. RANDOM 3D ARRAY
# Replace values greater than 50 with 0
# ============================================================

print("\n===== 21. RANDOM 3D ARRAY =====")

a = np.random.randint(1, 101, (2, 3, 4))

print("Original array:")
print(a)

a[a > 50] = 0

print("After replacing values greater than 50:")
print(a)


# ============================================================
# 22. RANDOM 3D ARRAY STATISTICS
# Mean, Median, Standard Deviation, Variance,
# Minimum and Maximum
# ============================================================

print("\n===== 22. 3D ARRAY STATISTICS =====")

a = np.random.randint(1, 101, (3, 4, 5))

print("Random 3D Array:")
print(a)

print("Mean:", np.mean(a))
print("Median:", np.median(a))
print("Standard deviation:", np.std(a))
print("Variance:", np.var(a))
print("Minimum:", np.min(a))
print("Maximum:", np.max(a))


# ============================================================
# 23. FLATTEN 3D ARRAY
# ============================================================

print("\n===== 23. FLATTEN 3D ARRAY =====")

a = np.arange(1, 25).reshape(2, 3, 4)

print("Original 3D array:")
print(a)

b = a.flatten()

print("Flattened array:")
print(b)


# ============================================================
# 24. FLATTEN ARRAY 1 TO 27
# Calculate Sum, Average, Maximum and Minimum
# ============================================================

print("\n===== 24. FLATTEN AND STATISTICS =====")

a = np.arange(1, 28).reshape(3, 3, 3)

b = a.flatten()

print("Original 3D array:")
print(a)

print("Flattened array:")
print(b)

print("Sum:", np.sum(b))
print("Average:", np.mean(b))
print("Maximum:", np.max(b))
print("Minimum:", np.min(b))


# ============================================================
# 25. RANDOM 3D ARRAY AND BOOLEAN INDEXING
# Greater than 50, Even numbers, Less than average
# ============================================================

print("\n===== 25. RANDOM 3D ARRAY CONDITIONS =====")

a = np.random.randint(1, 101, (3, 4, 5))

print("Original 3D array:")
print(a)

b = a.flatten()

print("Flattened array:")
print(b)

print("Elements greater than 50:")
print(b[b > 50])

print("Even numbers:")
print(b[b % 2 == 0])

average = np.mean(b)

print("Average:", average)

print("Elements less than average:")
print(b[b < average])
