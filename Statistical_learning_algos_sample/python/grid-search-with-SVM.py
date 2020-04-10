from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC
paramter = [{
	"C" : [1, 10, 100, 1000],
	"gamma" : [1, 0.1, 0.01, 0.001, 0.0001],
	"kernel" : ["rbf"]
}]

classifier = GridSearchCV(SVC(), paramter, cv=5, scoring="accuracy")
classifier.fit(X_train, y_train)
print(classifier.best_params_)