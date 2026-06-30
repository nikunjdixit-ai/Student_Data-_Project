from agents.data_loading import load_data
from agents.inspector import inspect_data
from agents.cleaner import clean_data
from agents.transformer import transform_data
from agents.filter import filter_data
from agents.analysis import analyze_data    # Module 6
from agents.sorting import sort_by_marks, sort_by_attendance, sort_by_study_hours  
from agents.grouping import grouping_analysis
from agents.statistics import statistical_analysis

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

print("\n📊 Students sorted by Marks")
sorted_marks = sort_by_marks(df)

print("\n📊 Students sorted by Attendance")
sorted_attendance = sort_by_attendance(df)

print("\n📊 Students sorted by Study Hours")
sorted_hours = sort_by_study_hours(df)

sorted_marks.to_csv("output/sorted_by_marks.csv", index=False)
sorted_attendance.to_csv("output/sorted_by_attendance.csv", index=False)
sorted_hours.to_csv("output/sorted_by_study_hours.csv", index=False)

print("\nSorting Files Saved Successfully!")

group_results = grouping_analysis(df)
group_results["Average Marks by Grade"].to_csv("output/avg_marks_by_grade.csv")
group_results["Count Students by Grade"].to_csv("output/count_students_by_grade.csv")
group_results["Average Attendance by Grade"].to_csv("output/avg_attendance_by_grade.csv")
print("\nGrouping Files Saved Successfully!")

stats_results = statistical_analysis(df)
