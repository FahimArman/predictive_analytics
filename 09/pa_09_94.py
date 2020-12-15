from sklearn.svm import SVC

poly_kernel_svm_clf = Pipeline([
						("scaler", StandardScaler()),
						("svm_clf", SVC(kernel="poly", degree=3, coef0=1, C=5))
						])

poly_kernel_svm_clf.fit(X, y)
