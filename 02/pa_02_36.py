import numpy as np

a3 = np.array([[3.0,5,7],[1,-1,1],[1,2,-5]])
y = np.array([10,3,-4])

#a3 = np.array([[-3,-5,2],[2,0,-1],[1,5,5]])
#y = np.array([-1,-3,-2])

x = np.linalg.solve(a3,y)
print("-" * 20)
print(x)
print("-" * 20)


