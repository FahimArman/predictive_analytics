from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PolynomialFeatures

polynomial_svm_clf = Pipeline([
					("poly_features", PolynomialFeatures(degree=3)),
					("scaler", StandardScaler()),
					("svm_clf", LinearSVC(C=10, loss="hinge"))
					])

polynomial_svm_clf.fit(X, y)
