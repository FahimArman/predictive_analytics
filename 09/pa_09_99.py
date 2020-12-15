from sklearn.svm import SVC

rbf_kernel_svm_clf = Pipeline([
							("scaler", StandardScaler()),
							("svm_clf", SVC(kernel="rbf", gamma=5, C=0.001))
							])

rbf_kernel_svm_clf.fit(X, y)
