def filter_data(df):

    topper = df[df["Marks"] > 90]
    failed = df[df["Result"] == "Fail"]
    attendance = df[df["Attendance"] < 75]
    study = df[df["StudyHours"] > 8]

    print("\nTop Performers")
    print(topper.head())

    print("\nFailed Students")
    print(failed.head())

    print("\nAttendance Below 75")
    print(attendance.head())

    print("\nStudy Hours Above 8")
    print(study.head())

    return topper, failed, attendance, study