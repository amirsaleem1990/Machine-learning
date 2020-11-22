import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
def new_line():
    print("-------------------------")

def plot_numerical_columns(col_name):
    df[col_name].plot(figsize=(13,8));
    plt.title(col_name, size=18);
    plt.axhline(y=df[col_name].mean(), color='red');
    plt.axhline(y=df[col_name].median(), color='green');
    plt.legend(['Actual', 'Mean', 'Median']);
    plt.show()

    df[col_name].sort_values().reset_index(drop=True).plot(figsize=(13,8));
    plt.title(col_name+" (SORTED)", size=18);
    plt.axhline(y=df[col_name].mean(), color='red');
    plt.axhline(y=df[col_name].median(), color='green');
    plt.legend(['Actual', 'Mean', 'Median']);
    plt.show()

    df[col_name].plot(kind="box", figsize=(13,8))
    plt.title(col_name, size=18);
    plt.xlabel("");
    plt.show()

def plot_date_columns(col_name):

    df[col_name].plot(figsize=(15,7), grid=True);
    plt.xlabel("Index", size=14);
    plt.ylabel("Date", size=14);
    plt.title(col_name + " Graph", size=18);
    plt.show();

    df[col_name].sort_values().reset_index(drop=True).plot(figsize=(15,7), grid=True);
    plt.xlabel("Index (sorted)", size=14);
    plt.ylabel("Year", size=14);
    plt.title(col_name + " Graph", size=18);
    plt.show();

    (df[col_name].dt.year.value_counts(sort=False).sort_index() / len(df) * 100).plot(kind="bar", figsize=(15,7), grid=True);
    plt.xlabel("Year", size=14);
    plt.ylabel("Ratio (1-100)", size=14);
    plt.title(col_name + " year Frequency Graph", size=18);
    plt.show();

    (df[col_name].dt.month.value_counts().sort_index()/len(df) * 100).plot(kind="bar", figsize=(15,7), grid=True);
    plt.xlabel("Month", size=14);
    plt.ylabel("Ratio (1-100)", size=14);
    plt.title(col_name + " month Frequency Graph", size=18);
    plt.show();

    (df[col_name].dt.day.value_counts().sort_index()/len(df) * 100).plot(kind="bar", figsize=(15,7), grid=True);
    plt.xlabel("Day", size=14);
    plt.ylabel("Ratio (1-100)", size=14);
    plt.title(col_name + " Day Frequency Graph", size=18);
    plt.show();

def plot_catagorical_columns(cat_variable):
    (df[cat_variable].value_counts() / len(df) * 100).plot.bar(figsize=(15,6), grid=True);
    plt.title(cat_variable, size=18, color='r');
    plt.xlabel("Catagory", size=14, color='r');
    plt.ylabel("Ratio (1-100)", size=14, color='r');
    plt.show()

def data_shape():
    return f"The Data have:\n\t{df.shape[0]} rows\n\t{df.shape[1]} columns\n"
#===
df = pd.read_csv("data.csv", date_parser=True)
# df = pd.read_csv("df_only_selected_columns_using_PCA.csv", date_parser=True)
new_line()
print(data_shape())
#===
new_line()
print(f"Columns types distribution:\n\n{df.dtypes.value_counts()}")
#---------------------------------------- NA
a = df.isna().sum().where(lambda x:x>0).dropna()
if a.size:
    new_line()
    print(f"There are {len(a)} (out of {df.shape[1]}, [{round(len(a)/df.shape[1]*100)}%]) columns that contains 1 or more NA")
#===
a = a.sort_values()/len(df)*100
if (a == 100).sum():
    new_line()
    df.drop(columns=a[a==100].index, inplace=True)
    print(f"There are {(a == 100).sum()} columns that are all Missing values, so we droped those.\nNow {data_shape()}\n\nDropped columns names:")
    for i in a[a==100].index:
        print("\t",i)
    a = a[a != 100]
#===
x = df[a.index].dtypes.value_counts()
if x.size:
    new_line()
    print(f"NA columns data type Distribution:\n\n{x}")
del x
#===
new_line()
if a.size:
    print(f"NaN Ratio (0-100)\n\n{a}")
else:
    print("Now There is no NaN value in our Data")
#===
if a.size:
    new_line()
#     is ko uncomment karna h
    # ans = input("Are you need to remove some columns?[y|n]")
    ans = "n"
    if ans == "y":
        to_remove = input("Please Enter columns names delimated by $\neg:Columns_1$Columns_2").split("$")
        df.drop(columns=to_remove, inplace=True)
        print(f"Now {data_shape()}")
#===
# IMPUTING missing values??????????????
#===
# --------------------------------------------------------- Unique values
# only_one_unique_value = df.nunique().where(lambda x:x == 1).dropna()
# if only_one_unique_value.size:
#     new_line()
#     df.drop(columns=only_one_unique_value.index, inplace=True)
#     print(f"There are {only_one_unique_value.size} variables That have only one unique value, so we drop those.\n\nNow {data_shape()}\n\nThose columns names in order:\n")
#     for i in only_one_unique_value.index.sort_values():
#         print(i)
# del only_one_unique_value
# #===
# all_values_are_unique = df.apply(lambda x:x.is_unique).where(lambda x:x==True).dropna()
# if all_values_are_unique.size:
#     new_line()
#     df.drop(columns=all_values_are_unique.index, inplace=True)
#     print(f"There are {all_values_are_unique.size} column/s that have all unique values, so no value repeatation, we droped those columns.\n\nNow {data_shape()}\nThose column/s name/s are:\n")
#     for i in f.index:
#         print("\t", i)
# del all_values_are_unique
#===
catagorical_columns = df.head().select_dtypes("O").columns
numerical_columns   = df.head().select_dtypes("number").columns
date_columns        = []
#===
for i in catagorical_columns:
    try:
        df[i] = pd.to_datetime(df[i])
        date_columns.append(i)
    except:
        pass
date_columns
#===
#===

#===
# "O"
# int
# float
# bool
# '<M8[ns]'
#===

#===

#===

#===

#===

#===

#===

#===

#===

#===

#===

#===

#===
