from sklearn import tree
# intiate classification tree object
classifier = tree.DecisionTreeClassifier()

# train the model
classifier = classifier.fit(X, y)

# predict on test set
classifier.predict(X_test)

# predict probability of classes
classifier.predict_proba(X_test)

# plot the tree
tree.plot_tree(classifier.fit(X, y))