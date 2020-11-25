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


df = pickle.load(open("df.pkl", "rb"))

# if df[target_variable].nunique() == 2:
#     print("\n-------------------- This is Binary Classification problem --------------------\n")
#     print("''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''")
# else:
#     print("\n-------------------- This is Multiclass Classification problem --------------------\n")
#     print("'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''")
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
target_variable = "STATUS_CODE"

for col in df.columns:
    df[col] = LabelEncoder().fit_transform(df[col].astype(str))

train_X, test_X, train_y, test_y = train_test_split(df.drop(columns=target_variable), df[target_variable])

clf=RandomForestClassifier(n_estimators=200).fit(train_X, train_y)
(clf.predict(test_X) == test_y).mean()



# ================================================================================================================ END Modeling
