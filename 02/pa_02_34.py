import numpy as np

a2 = np.array([[2.0,3.0],[0.0,0.0],[-3.0,2.0]])
b2 = np.array([[1.0,1.0],[0.0,2.0],[0.0,-2.0]])

#a2 = np.array([[1.0,-7],[-1,-9],[-10,1]])
#b2 = np.array([[1.0,1.0,7.0,4.0],[-1,10,2,3]])

#a2 = np.array([[2],[20],[18]])
#b2 = np.array([[13],[19],[-5]])
#316

#a2 = np.array([[1.0,-10],[-4,5],[-8,-4]])
#b2 = np.array([[1.0,6,6,2],[0,-8,0,-7]])

#matrix product
#c2 = a2.dot(b2)

#matrix dot product
c2 = a2.T.dot(b2)

print("-" * 20)
print(a2)
print("-" * 20)
print(a2.T)
print("-" * 20)
print(b2)
print("-" * 20)
print("\nAnswer: \n")
print("-" * 20)
print(c2)
print("-" * 20)
