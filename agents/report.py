
import pandas as pd

def generate_report(df):

    print("\n📑 Generating Report...")

    total_students = len(df)
    passed_students = (df['Result'] == 'Pass').sum()
    failed_students = (df['Result'] == 'Fail').sum()

    highest_marks = df['Marks'].max()
    lowest_marks = df['Marks'].min()
    average_marks = df['Marks'].mean()

    attendance_col = [col for col in df.columns if "attendance" in col.lower()][0]
    average_attendance = df[attendance_col].mean()

    grade_distribution = df['Grade'].value_counts().to_dict()

    report = {
        "Total Students": total_students,
        "Passed Students": passed_students,
        "Failed Students": failed_students,
        "Highest Marks": highest_marks,
        "Lowest Marks": lowest_marks,
        "Average Marks": average_marks,
        "Average Attendance": average_attendance,
        "Grade Distribution": grade_distribution
    }

    pd.DataFrame([report]).to_csv("output/report.csv", index=False)

    print("\n✅ Report Saved Successfully!")

    return report
