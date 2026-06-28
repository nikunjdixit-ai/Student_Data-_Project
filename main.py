from agents.data_loading import load_data
from agents.inspector import inspect_data
from agents.cleaner import clean_data
from agents.transformer import transform_data
from agents.filter import filter_data
from agents.analysis import analyze_data   # Module 6

df = load_data()

inspect_data(df)

df = clean_data(df)

df = transform_data(df)

print("\nUpdated Dataset")
print(df.head())

topper, failed, attendance, study = filter_data(df)

topper.to_csv("output/topper.csv", index=False)
failed.to_csv("output/failed_students.csv", index=False)
attendance.to_csv("output/attendance_below_75.csv", index=False)
study.to_csv("output/study_hours_above_8.csv", index=False)

print("\nFiltered Files Saved Successfully!")

analyze_data(df)