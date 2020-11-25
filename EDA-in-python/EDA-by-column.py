from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn import metrics
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
    # target_variable = "STATUS_CODE"
    # df = pickle.load(open("df.pkl", "rb"))
    df = pd.concat([
                    df.select_dtypes(exclude = "O"),
                    pd.get_dummies(df.drop(columns=target_variable).select_dtypes("O")),
                    df[[target_variable]]
                    ], 1)

    train_X, test_X, train_y, test_y = train_test_split(df.drop(columns=target_variable), df[target_variable])
    clf = LogisticRegression().fit(train_X, train_y)
    predictions = clf.predict_proba(test_X)
    predictions = pd.Series(predictions[:, 0])
    lst = []
    for thresh in np.linspace(predictions.min(), predictions.max(), 50)[1:]:
        pred = predictions < thresh

        pred.loc[pred == True] = clf.classes_[0]
        pred.loc[pred == False] = clf.classes_[1]

        test_y = test_y.reset_index(drop=True)
        lst.append((thresh, (pred == test_y).mean()*100))
    pd.DataFrame(lst, columns=["Thresold", "Accurecy(1-100)"]).plot(x="Thresold", y="Accurecy(1-100)", grid=True, figsize=(18,7));
    plt.title("Accurecy at diffrent Thresolds", size=18, color='red');
    plt.xlabel("Thresold", size=14, color='red');
    plt.ylabel("Accuracy (1-100)", size=14, color='red');
    plt.show()



# else:
#     print("\n-------------------- This is Multiclass Classification problem --------------------\n")
#     print("'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''")

    # df.loc[:, df.select_dtypes("O").columns] = df.select_dtypes("O").apply(lambda x: pd.Series(LabelEncoder().fit_transform(x.astype(str))).astype(str))
    # train_X, test_X, train_y, test_y = train_test_split(df.drop(columns=target_variable), df[target_variable])
    #
    # clf=RandomForestClassifier(n_estimators=1000).fit(train_X, train_y)
    # predictions = clf.predict(test_X)
    # feature_imp = pd.Series(clf.feature_importances_,index=train_X.columns).sort_values(ascending=False)
    # if feature_imp.size > 30:
    #     feature_imp = feature_imp.head(30)
    # feature_imp.plot(kind='barh', figsize=(17,10), grid=True);
    # plt.title("Feature importances Graph", size=18, color='red');
    # plt.xlabel("Importance", size=14, color='red');
    # plt.ylabel("Feature", size=14, color='red');
    # plt.show()
    # # ====
    # f = (test_y, predictions)
    # f_int = (test_y.astype(int), predictions.astype(int))
    #
    # print(f"accuracy_score: {metrics.accuracy_score(*f)}")
    # print(f"f1_score: {metrics.f1_score(*f_int)}")
    #
    # metrics.plot_roc_curve(clf, test_X, test_y);
    # plt.title("ROC curve plot");
    # plt.show();
    #
    # metrics.ConfusionMatrixDisplay(metrics.confusion_matrix(*f)); plt.show()
    #
    # metrics.plot_confusion_matrix(clf, test_X, test_y);
    # plt.title("Confusion matrix");
    # plt.show()
    #
    # metrics.plot_precision_recall_curve(clf, test_X, test_y);
    # plt.title("Precision recall curve");
    # plt.show()
# ================================================================================================================ END Modeling
