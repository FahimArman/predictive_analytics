import numpy as np

B = np.array([[0.0,1],[2,3.5],[-1.2,0]])

print("B ndim: ", B.ndim)
print("B shape: ", B.shape)
print("B size: ", B.size)
print("B data type: ", B.dtype)
print("-" * 20)
print(B)
print("-" * 20)

C = B.T
print("-" * 20)
print(C)
print("-" * 20)
print("C ndim: ",C.ndim)
print("C shape: ", C.shape)
print("C size: ", C.size)
print("C data type: ", C.dtype)
print("-" * 20)
