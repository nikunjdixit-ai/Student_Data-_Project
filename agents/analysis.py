import pandas as pd

def analyze_data(df):
    print("\n========== DATA ANALYSIS ==========\n")

    print("Average Marks:", df["Marks"].mean())
    print("Highest Marks:", df["Marks"].max())
    print("Lowest Marks:", df["Marks"].min())

    print("Average Attendance:", df["Attendance"].mean())
    print("Average Study Hours:", df["StudyHours"].mean())

    total = len(df)
    passed = (df["Result"] == "Pass").sum()
    failed = (df["Result"] == "Fail").sum()

    print("Pass Percentage:", (passed / total) * 100, "%")
    print("Fail Percentage:", (failed / total) * 100, "%")

    print("\nGrade Distribution:")
    print(df["Grade"].value_counts())

    print("\n========== ANALYSIS COMPLETED ==========")