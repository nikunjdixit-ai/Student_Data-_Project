import matplotlib.pyplot as plt

df['Grade'].value_counts().plot(kind='bar')
plt.title("Grade Distribution")
plt.savefig("output/grade_distribution.png")
plt.close()

plt.scatter(df['Study Hours'], df['Marks'])
plt.title("Marks vs Study Hours")
plt.savefig("output/marks_vs_study_hours.png")
plt.close()

plt.scatter(df['Attendance (%)'], df['Marks'])
plt.title("Attendance vs Marks")
plt.savefig("output/attendance_vs_marks.png")
plt.close()

print("\n✅ Visualizations saved in output folder!")
