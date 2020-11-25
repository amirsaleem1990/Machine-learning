import pickle
import pprint
from sklearn.ensemble import RandomForestRegressor
from pandas_profiling import ProfileReport
from dateutil import relativedelta
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")
from sklearn.model_selection import train_test_split
from statsmodels.regression.linear_model import OLS

def new_line():
    print("-------------------------")



# if df[target_variable].nunique() == 2:
#     print("\n-------------------- This is Binary Classification problem --------------------\n")
#     print("''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''")
# else:
#     print("\n-------------------- This is Multiclass Classification problem --------------------\n")
#     print("'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''")


from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn import metrics
df = pickle.load(open("df.pkl", "rb"))
target_variable = "STATUS_CODE"

df.loc[:, df.select_dtypes("O").columns] = df.select_dtypes("O").apply(lambda x: pd.Series(LabelEncoder().fit_transform(x.astype(str))).astype(str))
train_X, test_X, train_y, test_y = train_test_split(df.drop(columns=target_variable), df[target_variable])

clf=RandomForestClassifier(n_estimators=1000).fit(train_X, train_y)
predictions = clf.predict(test_X)
feature_imp = pd.Series(clf.feature_importances_,index=train_X.columns).sort_values(ascending=False)
if feature_imp.size > 30:
    feature_imp = feature_imp.head(30)
feature_imp.plot(kind='barh', figsize=(17,10), grid=True);
plt.title("Feature importances Graph", size=18, color='red');
plt.xlabel("Importance", size=14, color='red');
plt.ylabel("Feature", size=14, color='red');
plt.show()
# ====
f = (test_y, predictions)
f_int = (test_y.astype(int), predictions.astype(int))

print(f"accuracy_score: {metrics.accuracy_score(*f)}")
print(f"f1_score: {metrics.f1_score(*f_int)}")

metrics.plot_roc_curve(clf, test_X, test_y);
plt.title("ROC curve plot");
plt.show();

metrics.ConfusionMatrixDisplay(metrics.confusion_matrix(*f)); plt.show()

metrics.plot_confusion_matrix(clf, test_X, test_y);
plt.title("Confusion matrix");
plt.show()

metrics.plot_precision_recall_curve(clf, test_X, test_y);
plt.title("Precision recall curve");
plt.show()









# ================================================================================================================ END Modeling
