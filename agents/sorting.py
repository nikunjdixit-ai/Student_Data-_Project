import pandas as pd

def sort_by_marks(df):

    sorted_df = df.sort_values(by="Marks", ascending=False)
    print("\n--- Students Sorted by Marks ---")
    print(sorted_df.head(10))
    return sorted_df

def sort_by_attendance(df):
    sorted_df = df.sort_values(by="Attendance", ascending=False)
    print("\n--- Students Sorted by Attendance ---")
    print(sorted_df.head(10))
    return sorted_df

def sort_by_study_hours(df):
    sorted_df = df.sort_values(by="StudyHours", ascending=False)
    print("\n--- Students Sorted by Study Hours ---")
    print(sorted_df.head(10))
    return sorted_df

