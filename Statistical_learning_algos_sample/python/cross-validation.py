from sklearn.model_selection import KFold
kf = KFold(n_splits=5)
kf.get_n_splits(X_train)