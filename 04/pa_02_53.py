import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error

houses = np.genfromtxt('rtown.csv', delimiter=',', skip_header=1, usecols=(2,3))

X = houses[:,0].reshape(-1,1)
y = houses[:,1].reshape(-1,1)

# extend features: 2nd degree polynomial
pf2 = PolynomialFeatures(degree=2)
Xpoly = pf2.fit_transform(X)

# fit linear model
model = linear_model.LinearRegression()
model.fit(Xpoly, y)

# create a regression line
x0 = np.min(X) - 9 # start before smallest house
xn = np.max(X) + 10 # finish after largest house

X1 = np.arange(x0,xn).reshape(-1,1)
X1poly = pf2.fit_transform(X1)
pred = model.predict(X1poly)

plt.plot(X1,pred, color='white')
plt.plot(X,y,'b.')
plt.xlabel("House size (sqm)", fontsize=16)
plt.ylabel("Price ($)", rotation=90, fontsize=16)
plt.savefig('rtown.png', dpi=300)
plt.plot(X1,pred, color='m')
plt.savefig('polyreg2.png', dpi=300)
plt.show()
