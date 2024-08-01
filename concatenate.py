import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

con_ar = np.concatenate((a, b))

print("1D array 'a':", a)
print("1D array 'b':", b)
print("Concatenated array:", con_ar)