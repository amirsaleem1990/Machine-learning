from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
logmodel = LogisticRegression()
logmodel.fit(X_train,Y_train.astype(int))
Y_predict = logmodel.predict(X_test)

#These are the metrics for the Classifier
print(classification_report(Y_test.astype(int),Y_predict.astype(int)))

