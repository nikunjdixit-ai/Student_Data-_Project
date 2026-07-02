# Student Performance Data Handling and Analysis System

## 📘 Overview
This project processes student performance data using **Python** and **Pandas**.  
It demonstrates the complete data lifecycle: loading, cleaning, transforming, analyzing, and reporting.  
Bonus tasks include **Matplotlib visualizations** and **Excel export**.

---

## 🎯 Features
- **Data Loading**: Read CSV, preview records, dataset shape, column names, data types.  
- **Data Cleaning**: Handle missing values, remove duplicates, validate entries.  
- **Data Transformation**: Add Grade, Pass/Fail, and Performance Score.  
- **Data Filtering**: Generate datasets for toppers, failed students, low attendance, and high study hours.  
- **Data Analysis**: Compute averages, percentages, distributions.  
- **Sorting & Grouping**: Sort by marks, attendance, study hours; group by grade.  
- **Statistical Analysis**: Mean, median, mode, standard deviation, variance, correlation.  
- **Report Generation**: Final report in CSV and Excel formats.  
- **Visualizations**: Grade distribution, Marks vs Study Hours, Attendance vs Marks.  

---

## 📂 Folder Structure

Student_Data_Project/
│── data/
│   └── student_dataset_v2.csv
│── output/
│   ├── cleaned_data.csv
│   ├── toppers.csv
│   ├── failed_students.csv
│   ├── report.csv
│   ├── report.xlsx
│   ├── grade_distribution.png
│   ├── marks_vs_study_hours.png
│   └── attendance_vs_marks.png
│── src/
│   ├── main.py
│   ├── agents/
│   │   ├── data_loading.py
│   │   ├── inspector.py
│   │   ├── cleaner.py
│   │   ├── transformer.py
│   │   ├── filter.py
│   │   ├── analysis.py
│   │   ├── sorting.py
│   │   ├── grouping.py
│   │   ├── statistics.py
│   │   ├── report.py
│   │   └── visualization.py
│── README.md