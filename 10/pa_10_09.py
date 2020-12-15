from sklearn.neighbors import KNeighborsClassifier

clf = KNeighborsClassifier(n_neighbors=1)

clf.fit(X_train, y_train)

clf.predict(X_test)
