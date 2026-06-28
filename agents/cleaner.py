def clean_data(df):

    df = df.drop_duplicates()

    df = df.dropna()

    df = df[(df["Attendance"] >= 0) & (df["Attendance"] <= 100)]

    df = df[df["StudyHours"] >= 0]

    df = df[(df["Marks"] >= 0) & (df["Marks"] <= 100)]

    print("\nData Cleaned Successfully!")

    return df