def inspect_data(df):

    print("\n===== Dataset Information =====")
    df.info()

    print("\n===== Descriptive Statistics =====")
    print(df.describe())

    print("\n===== Missing Values =====")
    print(df.isnull().sum())

    print("\n===== Memory Usage =====")
    print(df.memory_usage())