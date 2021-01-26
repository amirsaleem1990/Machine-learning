# often in several real-world scenarios, it makes sense to also try and capture the interactions between these feature variables as a part of the input feature set

# build features up to the 2nd degree:
from sklearn.preprocessing import PolynomialFeatures
pf = PolynomialFeatures(degree=2, 
						interaction_only=False,  
                        include_bias=False)
res = pf.fit_transform(atk_def)
# We can see the degree of each feature in the above matrix as follows.
pd.DataFrame(pf.powers_, 
			 columns=['Attack_degree',
			 'Defense_degree'])
# Looking at this output, we now know what each feature actually represents from the degrees depicted here. Armed with this knowledge, we can assign a name to each feature now as follows. This is just for ease of understanding and you should name your features with better, easy to access and simple names.
intr_features = pd.DataFrame(res, columns=['Attack', 'Defense',  
                                           'Attack^2', 
                                           'Attack x Defense',  
                                           'Defense^2'])

# Binning, custom range binning
bin_ranges = [0, 15, 30, 45, 60, 75, 100]
bin_names = [1, 2, 3, 4, 5, 6]
df['Age_bin_custom_range'] = pd.cut(
								np.array(df.Age), 
								bins=bin_ranges)
df['Age_bin_custom_label'] = pd.cut(
							np.array(df.Age), 
							bins=bin_ranges,
							labels=bin_names)


# Adaptive Binning
The drawback in using fixed-width binning is that due to us manually deciding the bin ranges, we can end up with irregular bins which are not uniform based on the number of data points or values which fall in each bin. Some of the bins might be densely populated and some of them might be sparsely populated or even empty! Adaptive binning is a safer strategy in these scenarios where we let the data speak for itself! That’s right, we use the data distribution itself to decide our bin ranges.
Quantile based binning is a good strategy to use for adaptive binning.

quantile_list = [0, .25, .5, .75, 1.]
quantiles = df.Income.quantile(quantile_list)
quantile_labels = ['0-25Q', '25-50Q', '50-75Q', '75-100Q']
df.Income_quantile_range = pd.qcut( df.Income, q=quantile_list )
df.Income_quantile_label = pd.qcut( df.Income, q=quantile_list, labels=quantile_labels)

# get optimal lambda value for box-cox transformation:
l, opt_lambda = spstats.boxcox(df.column) # df.column must be positive
# apply box-cox transormation to the column with this lambda:
df.column = spstats.boxcox(df.column,lmbda=opt_lambda)


# calculate IQR
q25, q75 = np.percentile(data, 25), np.percentile(data, 75)
iqr = q75 - q25
cut_off = iqr * 1.5
lower, upper = q25 - cut_off, q75 + cut_off
df.column.between(lower,upper)


# to generate random Gaussian values with a mean of mean of 50 and a standard deviation of 5
data = 5 * np.random.randn(10000) + 50


# LOF (local outlier factor)
lof = LocalOutlierFactor()
yhat = lof.fit_predict(X_train)
# select all rows that are not outliers
mask = yhat != -1
X_train, y_train = X_train[mask, :], y_train[mask]
model = LinearRegression()
model.fit(X_train, y_train)
yhat = model.predict(X_test)


# Isolation Forest
iso = IsolationForest(contamination=0.1)
yhat = iso.fit_predict(X_train)
# select all rows that are not outliers
mask = yhat != -1
X_train, y_train = X_train[mask, :], y_train[mask]
model = LinearRegression()
model.fit(X_train, y_train)
yhat = model.predict(X_test)

# Minimum Covariance Determinant (MCD) 
from sklearn.covariance import EllipticEnvelope
# “contamination” argument that defines the expected ratio of outliers to be observed in practice. In this case, we will set it to a value of 0.01, found with a little trial and error.
# identify outliers in the training dataset
ee = EllipticEnvelope(contamination=0.01)
yhat = ee.fit_predict(X_train)
mask = yhat != -1
X_train, y_train = X_train[mask, :], y_train[mask]
model = LinearRegression()
model.fit(X_train, y_train)
yhat = model.predict(X_test)


# OneClassSVM
from sklearn.svm import OneClassSVM
# identify outliers in the training dataset
ee = OneClassSVM(nu=0.01)
yhat = ee.fit_predict(X_train)
# select all rows that are not outliers
mask = yhat != -1
X_train, y_train = X_train[mask, :], y_train[mask]
model = LinearRegression()
model.fit(X_train, y_train)
yhat = model.predict(X_test)

