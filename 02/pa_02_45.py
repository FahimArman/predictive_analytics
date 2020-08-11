import numpy as np

v4 = np.array([8.0,7.0])
#v4 = np.array([20.0,0,11,12])
#v4 = np.array([6,8,9,2,12,17])

#vector norm

l1 = np.linalg.norm(v4,1)
l2 = np.linalg.norm(v4)

print("-" * 20)
print(v4)
print("-" * 20)
print(l1)
print("-" * 20)
print(l2)
print("-" * 20)
