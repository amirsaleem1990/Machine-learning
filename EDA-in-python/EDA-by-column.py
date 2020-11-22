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
# df = pd.read_csv("data.csv", date_parser=True)
df = pd.read_csv("df_only_selected_columns_using_PCA.csv", date_parser=True)
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
only_one_unique_value = df.nunique().where(lambda x:x == 1).dropna()
if only_one_unique_value.size:
    new_line()
    df.drop(columns=only_one_unique_value.index, inplace=True)
    print(f"There are {only_one_unique_value.size} variables That have only one unique value, so we drop those.\n\nNow {data_shape()}\n\nThose columns names in order:\n")
    for i in only_one_unique_value.index.sort_values():
        print(i)
del only_one_unique_value
# #===
all_values_are_unique = df.apply(lambda x:x.is_unique).where(lambda x:x==True).dropna()
if all_values_are_unique.size:
    new_line()
    df.drop(columns=all_values_are_unique.index, inplace=True)
    print(f"There are {all_values_are_unique.size} column/s that have all unique values, so no value repeatation, we droped those columns.\n\nNow {data_shape()}\nThose column/s name/s are:\n")
    for i in all_values_are_unique.index:
        print("\t", i)
del all_values_are_unique
#===
catagorical_columns = df.head().select_dtypes("O").columns
numerical_columns   = df.head().select_dtypes("number").columns
date_columns        = []

for i in catagorical_columns:
    try:
        df[i] = pd.to_datetime(df[i])
        date_columns.append(i)
    except:
        pass

catagorical_columns = catagorical_columns.drop(date_columns)
if date_columns:
    date_columns = pd.Index(date_columns)
#===
if not catagorical_columns.append(numerical_columns).append(date_columns).is_unique:
    new_line()
    print("\nSome column/s repated in > 1 dtypes\n")
    dtypes = pd.DataFrame({"Column" : catagorical_columns.append(numerical_columns).append(date_columns),
                "dtype" : ['O']*len(catagorical_columns) + ['Number']*len(numerical_columns) + ['Date']*len(date_columns)})
    print(dtypes[dtypes.Column.isin(list(dtypes[dtypes.Column.duplicated()].Column.values))].to_string())
#===
x = df.columns.difference(
    catagorical_columns.append(numerical_columns).append(date_columns)
    )
if x.size:
    new_line()
    print("Some columns not included in any existing catagory, those:\n")
    for i in x:
        print(f"\t<{i}, with dtype of <{df[i].dtype}>")
#===
dtypes = pd.DataFrame({"Column" : catagorical_columns.append(numerical_columns).append(date_columns),
            "dtype" : ['O']*len(catagorical_columns) + ['Number']*len(numerical_columns) + ['Date']*len(date_columns)})
dtypes.dtype.unique()
#===
m = 0
for row in dtypes.iterrows():
    m += 1
    if m == 3:
        break
    column_name, type_ = row[1]
    x = df[column_name]
    print(f"\n\n\n============================= {column_name} =============================\n\n")
    new_line()
    print(f"Column Type     : {type_}")
    print(f"NA count        : {x.isna().sum()}")
    print(f"NA Ratio (1-100): {x.isna().mean()*100}")
    new_line()
    if x.isna().all():
        new_line()
        df.drop(columns=column_name, inplace=True)
        print("We dropped This column, because it is all Empty")
        continue
    if type_ in ["O", "Date"]:
        new_line()
        if x.is_unique:
            df.drop(columns=column_name, inplace=True)
            print(f"We dropped This column, because it's a {type_} columns, and it's all values are unique")
            continue
    if x.nunique() == 1:
        new_line()
        df.drop(columns=column_name, inplace=True)
        print(f"We dropped This column, because There is only one unique value")
        continue


    if type_ == "Number":

        # f = x.describe()
        # f['Nunique'] = x.nunique()
        # f['Nunique ratio'] = f.loc["Nunique"] / f.loc["count"] * 100
        # f['Outlies count'] = (((x - x.mean())/x.std()).abs() > 3).sum()
        # f['Outlies ratio'] = f.loc["Outlies count"] / f.loc["count"] * 100
        # f['Nagative values count'] = (x < 0).sum()
        # f['Nagative values ratio'] = f['Nagative values count'] / f['count'] * 100

        ff = [x.count(), x.isna().sum(), x.mean(), x.std(), x.min()]
        ff += x.quantile([.25,.5,.75]).to_list()
        ff += [x.max(), x.nunique(), (((x - x.mean())/x.std()).abs() > 3).sum(), (x < 0).sum()]

        f = pd.DataFrame(ff, index=['Count', 'NA', 'Mean', 'Std', 'Min', '25%', '50%', '75%', 'Max', 'Nunique', 'Outlies', 'Nagetive'], columns=['Count'])
        f['Ratio'] = f.Count / x.count() * 100
        f.loc['Mean' : 'Max', 'Ratio'] = None

        new_line()
        print(f.round(2).to_string())
        plot_numerical_columns(column_name)

    elif type_ == "O":
        # f = x.describe()
        # f = x.agg(['count', pd.Series.nunique])
        # f['len'] = len(x)
        # f['Na count'] = x.isna().sum()
        # f['Na ratio'] = f['Na count'] / f['count'] * 100
        # f['Most frequent'] = x.mode().values[0]
        # f['Most frequent count'] = (x == f['Most frequent']).sum()
        # f['Most frequent ratio'] = f['Most frequent count'] / f['count'] * 100
        # f['Least frequent'] = x.value_counts().tail(1).index[0]
        # f['Least frequent count'] = (x == f['Least frequent']).sum()
        # f['Least frequent ratio'] = f['Least frequent count'] / f['count'] * 100
        # f['Values occured only once count'] = x.value_counts().where(lambda x:x==1).dropna().size
        # f['Values occured only once Ratio'] = f['Values occured only once count'] / x.count() * 100

        l = x.count(), x.nunique(), len(x), x.isna().sum(), (x == x.mode().values[0]).sum(), (x == x.value_counts().tail(1).index[0]).sum(), x.value_counts().where(lambda x:x==1).dropna().size
        f = pd.DataFrame(l, index=['Count', 'Nunique', 'Len', 'NA', 'Most frequent', 'Least frequent', 'Values occured only once'], columns=['Counts'])
        f['Ratio'] = (f.Counts / x.count() * 100).round(4)
        f.loc[['Count', 'Len'], 'Ratio'] = None

        new_line()
        print(f.to_string())

        new_line()
        if x.str.lower().nunique() != x.nunique():
            print(f"\n\nCase issue\n\tin orignal variable There are {x.nunique()} unique values\n\tin lower verstion there are   {x.str.lower().nunique()} unique values.")

        new_line()
        if x.str.strip().nunique() != x.nunique():
            print(f"\n\nSpace issue\n\tin orignal variable There are {x.nunique()} unique values\n\tin striped verstion there are {x.str.strip().nunique()} unique values.")

        new_line()
        plot_catagorical_columns(column_name)

    elif type == "Date":

        new_line()
        from dateutil import relativedelta
        rd = relativedelta.relativedelta( pd.to_datetime(x.max()), pd.to_datetime(x.min()))
        print(f"Diffrenece between first and last date:\n\tYears : {rd.years}\n\tMonths: {rd.months}\n\tDays  : {rd.days}\n\n")

        # f = pd.Series({'Count' : x.count(),
        #             'Nunique count' : x.nunique(),
        #             'Nunique ratio' : x.nunique() / x.count() * 100,
        #             'Most frequent value' : str(x.mode()[0]),
        #             'Least frequent value' :  x.value_counts().tail(1).index[0]
        #             })
        # f['Most frequent count'] = (x == f['Most frequent value']).sum()
        # f['Most frequent ratio'] = f['Most frequent count'] / f['Count'] * 100
        # f['Least frequent count'] = (x == f['Least frequent value']).sum()
        # f['Least frequent ratio'] = f['Least frequent count'] / f['Count'] * 100
        # f['Values occured only once count'] = x.value_counts().where(lambda x:x==1).dropna().size
        # f['Values occured only once Ratio'] = f['Values occured only once count'] / x.count() * 100

        ff = x.count(), x.nunique(), (x == x.mode().values[0]).sum(), (x == x.value_counts().tail(1).index[0]).sum(), x.value_counts().where(lambda x:x==1).dropna().size
        f = pd.DataFrame(ff, index=["Count", 'Nunique', 'Most frequent values', 'Least frequent values', 'Values occured only once count'], columns=['Counts'])
        f['Ratio'] = (f.Counts / x.count() * 100).round(4)

        new_line()
        print(f"\n{f.to_string()}\n\n")


        f = set(np.arange(x.dt.year.min(),x.dt.year.max()+1)).difference(
            x.dt.year.unique())
        if f:
            new_line()
            print(f"These Years (in order) are missing:\n")
            for i in f:
                print("\t", i, end=", ")
            print("\n\n")

        f = set(np.arange(x.dt.month.min(),x.dt.month.max()+1)).difference(
            x.dt.month.unique())
        if f:
            new_line()
            print(f"These Months (in order) are missing:\n")
            for i in f:
                print("\t", i, end=", ")
            print("\n\n")

        f = set(np.arange(x.dt.day.min(),x.dt.day.max()+1)).difference(
            x.dt.day.unique())
        if f:
            new_line()
            print(f"These Days (in order) are missing:\n")
            for i in f:
                print("\t", i, end=", ")
            print("\n\n")

        new_line()
        plot_date_columns(column_name)
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
