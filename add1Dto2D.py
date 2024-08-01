import numpy as np

a = np.array([[1, 0, 0],
              [0, 1, 0],
              [0, 0, 1]])

b = np.array([1, 1, 1])

result = a + b

print("2D array 'a':\n", a)
print("1D array 'b':\n", b)
print("After adding array b to each row of of array a:\n", result)
