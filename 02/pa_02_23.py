import numpy as np

A = np.random.randint(10, size=(4,3))

print("A ndim: ", A.ndim)
print("A shape: ", A.shape)
print("A size: ", A.size)
print("A data type: ", A.dtype)
print("-" * 20)
print(A)
print("-" * 20)


B = np.array([[0.0,1],[2,-3.5],[-1.2,0]])

print("B ndim: ", B.ndim)
print("B shape: ", B.shape)
print("B size: ", B.size)
print("B data type: ", B.dtype)
print("-" * 20)
print(B)
print("-" * 20)
