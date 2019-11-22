from sklearn.linear_model import LinearRegression 
from sklearn.metrics import r2_score

x_train = df_train.as_matrix(['x'])
y_train = df_train.as_matrix(['y'])


x_test = df_test.as_matrix(['x'])
y_test = df_test.as_matrix(['y'])

clf = LinearRegression(normalize=True)
clf.fit(x_train,y_train)
y_pred = clf.predict(x_test)
print(r2_score(y_test,y_pred))
