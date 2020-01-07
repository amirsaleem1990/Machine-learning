from sklearn.model_selection import KFold
kf = KFold(n_splits=5)
kf.get_n_splits(X_train)


# stratified version(keep distribution of target variable is equal in all KFOLDS)
from sklearn.model_selection import StrafiedKFold
skf = StrafiedKFold(n_splits=5)
skf.get_n_splits(X_train, y_train)

