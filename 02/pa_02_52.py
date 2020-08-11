import numpy as np

#moore-penrose

A5 = 1.0 * np.random.randint(100,size=(5,3))

b = np.array([1.0,2.0,-1.0,4.0,-1.0])

A5inv = np.linalg.pinv(A5)

x = A5inv.dot(b)

print(A5)
print("-" * 20)
print(x)
print("-" * 20)
print(b)
print("-" * 20)
print("-" * 20)
print(A5.dot(x))
