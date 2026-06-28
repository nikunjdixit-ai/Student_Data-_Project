import pandas as pd

def load_data():

    df = pd.read_csv("data/student_dataset_v2.csv")

    print("\n===== First 5 Records =====")
    print(df.head())

    print("\n===== Last 5 Records =====")
    print(df.tail())

    print("\n===== Shape =====")
    print(df.shape)

    print("\n===== Column Names =====")
    print(df.columns)

    print("\n===== Data Types =====")
    print(df.dtypes)

    return df