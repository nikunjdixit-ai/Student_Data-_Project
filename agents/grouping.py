import pandas as pd 

def grouping_analysis(df):
    avg_marks = df.groupby("Grade")["Marks"].mean()
    count_students = df.groupby("Grade")["ID"].count()
    avg_attendance = df.groupby("Grade")["Attendance"].mean()

    print("/n======Average Marks======")
    print(avg_marks)
    
    print("/n=======Average Attendance=======")
    print(avg_attendance)

    print("/n=======Count of Students==========")
    print(count_students)

    return {
        "Average Marks by Grade": avg_marks,
        "Count Students by Grade": count_students,
        "Average Attendance by Grade": avg_attendance
    }

