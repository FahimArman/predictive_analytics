from sklearn.linear_model import Lasso
# modelling
lasso_reg = Lasso(alpha=0.1, max_iter=1e5)
# default for max_iter=1e3
lasso_reg.fit(X, y)
# prediction
lasso_reg.predict(X1)
