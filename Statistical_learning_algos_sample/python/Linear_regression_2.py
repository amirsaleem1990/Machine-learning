from sklearn import linear_model
regress = linear_model.LinearRegression()
regress = regress.fit(X, y)
regress.predict(X_test)