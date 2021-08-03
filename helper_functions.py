import pandas 
import numpy 
from sklearn.model_selection import train_test_split


def null_count(df): # Counts number of nulls in DataFrame
    return df.isna().sum().sum()

def splitty(df, frac): # Splits DataFrame based on frac size
    train_80 = train_test_split(df, train_size= frac)
    return train_80

def randomize(df, seed): # Randomizes DataFrame first with columns then rows
    df_columns = df.sample(n= df.columns.value_counts().sum(), axis=1,  random_state = seed)
    df_rows = df_columns.sample(n= len(df), random_state = seed)
    return df_rows

    