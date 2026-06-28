def transform_data(df):

    grade = []
    result = []

    for mark in df["Marks"]:

        if mark >= 90:
            grade.append("A")
        elif mark >= 75:
            grade.append("B")
        elif mark >= 60:
            grade.append("C")
        elif mark >= 40:
            grade.append("D")
        else:
            grade.append("F")

        if mark >= 40:
            result.append("Pass")
        else:
            result.append("Fail")

    df["Grade"] = grade
    df["Result"] = result

    print("New Columns Added Successfully!")
    df.to_csv("output/updated_dataset.csv", index=False)

    print("File Saved Successfully!")

    return df