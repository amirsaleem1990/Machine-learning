from sklearn.model_selection import RandomizedSearchCV
from sklearn.svm import SVC
paramter = [{
	"C" : stats.uniform(2,10),
	"gamma" : stats.uniform(0.1, 1),
	"kernel" : ["rbf"]
}]

classifier = RandomizedSearchCV(SVC(), paramter, cv=5, scoring="accuracy")
classifier.fit(X_train, y_train)
print(classifier.best_params_)