import numpy as np

a = np.array([1, 2, 3])
b = np.array([[1,2,3],[4,5,6]])
c = np.zeros((2,2))
d = np.ones((1,2))
e = np.full((2,2), 7)

print(a)

print(np.add(b, a))
print(np.subtract(b, a))
print(np.multiply(b, a))
print(np.divide(b, a))
print(np.sqrt(b))

