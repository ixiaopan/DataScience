import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats

# === EDA for categorical variables ===
def categorical_counts_stats(df, N = 5):
    """
    print the counts of unique values for categorical and object values.
    """

    columns = df.select_dtypes(include=['object', 'category']).columns
    print(f'There are {len(columns)} categorical variables!')

    for col in columns:
        print("Categrorical variable: " + col)

        cate_counts = df[col].value_counts()
        cate_len = len(cate_counts)

        # reshape
        cate_counts = cate_counts.reset_index().rename(columns={"index": col, col: "Count"})

        print(cate_counts[:min(N, cate_len)])
    

def categorical_eda(df, columns=None, hue=None):
    """
    Plot count distribution of categorical data
    """

    # categorical_counts_stats(df)

    if columns is None:
        columns = df.select_dtypes(include='category').columns
    
    col = 2
    row = (len(columns) // col) + (0 if len(columns)%col==0 else 1)
    fig, ax = plt.subplots(row, col, figsize=(14, 4*row), gridspec_kw={'hspace': 0.4, 'wspace': 0.2})
    for i, column in enumerate(columns):
        ax_i = ax[i//col, i%col]
        g = sns.countplot(data=df, x=column, hue=hue, ax=ax_i)
        g.set_xticklabels(ax_i.get_xticklabels(), rotation=20)
        ax_i.yaxis.label.set_visible(False)

    plt.show()


# === Diagnosis ===
def check_duplicated(df, remove=False):
    duplicated_flag = df.duplicated()

    if sum(duplicated_flag) > 0:
        print(f"{sum(df.duplicated())} duplicated rows!")

        print('Remove duplicates...')

        df = df.drop_duplicates()

        check_duplicated(df)
        
        return df
    else:
        print('No duplicated rows!')

    # return duplicated_flag

def missing_heatmap(df):
    fig, ax = plt.subplots(1, 2, figsize=(16, 6))

    # plot 1
    sns.heatmap(df.isna(), ax=ax[0])
    
    null_values_stats = df.isnull().sum(axis=0) # for each column
    if np.all(null_values_stats == 0):
        print('No missing values!')
    else:
        zero_null_values_stats = (null_values_stats / len(df)).sort_values(ascending=False)
        sns.set_color_codes("muted")
        sns.barplot(x=zero_null_values_stats.values, y=zero_null_values_stats.index, color='b', ax=ax[1])
    plt.show()
    
    return df.columns[df.isna().any(axis=0)]

def missing_table(df, pct=0):
    null_values = df.isnull().sum(axis=0)

    if np.all(null_values == 0):
        return print('No missing values!')
    
    threshold = len(df) * pct
    null_values = pd.DataFrame(null_values[null_values > threshold], columns=['counts'])
    null_values['percent'] = round(null_values['counts'] / len(df) *100)

    return null_values.sort_values('percent',ascending=False)


def cutIQR(cleaned_df, col, q1=0.25, q2=0.75, r=1.5):
    Q1 = cleaned_df[col].quantile(q1)
    Q3 = cleaned_df[col].quantile(q2)
    IQR = Q3 - Q1

    lower = Q1 - r * IQR
    upper = Q3 + r * IQR
    
    cutted_df = cleaned_df[(cleaned_df[col] >= lower) & (cleaned_df[col] <= upper)]

    return cutted_df, upper


def zscore_outlier(data, threshold = 3):
    z_price = stats.zscore(data)

    indices = np.zeros(len(data))
    indices[np.where(z_price > threshold)] = 1

    plt.scatter(np.arange(len(data)), data, c=indices, cmap='RdBu')
    plt.show()
