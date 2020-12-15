from sklearn.linear_model import Ridge
# modelling
ridge_reg = Ridge(alpha=1)
ridge_reg.fit(X, y)
# prediction
ridge_reg.predict(X1)
