# Student Performance Analytics System

import pandas as pd
import numpy as np

# Read student data from CSV file
data = pd.read_csv("students.csv")

# Subjects included in the project
subjects = ["Python", "DBMS", "AIML"]

# Calculate total and average marks
data["Total"] = data[subjects].sum(axis=1)
data["Average"] = data[subjects].mean(axis=1).round(2)

# Find the grade of each student
def find_grade(avg):
    if avg >= 90:
        return "A+"
    elif avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 40:
        return "D"
    else:
        return "F"

data["Grade"] = data["Average"].apply(find_grade)

# Check whether students passed or failed
data["Result"] = np.where(
    (data[subjects] >= 35).all(axis=1),
    "Pass",
    "Fail"
)

# Display all student results
print("\nSTUDENT PERFORMANCE ANALYTICS SYSTEM")
print("=" * 45)

print("\nSTUDENT RESULTS")
print(data[[
    "Student_ID", "Name", "Department",
    "Total", "Average", "Grade", "Result"
]].to_string(index=False))

# Calculate class performance
print("\nCLASS PERFORMANCE")
print("-" * 30)

print("Total students:", len(data))
print("Class average:", round(data["Average"].mean(), 2))
print("Students passed:", (data["Result"] == "Pass").sum())
print("Students failed:", (data["Result"] == "Fail").sum())

# Find the topper
topper = data.loc[data["Average"].idxmax()]

print("\nTOPPER")
print("Name:", topper["Name"])
print("Department:", topper["Department"])
print("Average marks:", topper["Average"])

# Subject-wise average marks
print("\nSUBJECT-WISE AVERAGES")
for subject in subjects:
    print(subject, ":", round(data[subject].mean(), 2))

# Check students with attendance below 75%
print("\nLOW ATTENDANCE STUDENTS")
low_attendance = data[data["Attendance"] < 75]

if low_attendance.empty:
    print("No students found.")
else:
    print(low_attendance[["Name", "Attendance"]].to_string(index=False))

# Save the results in a new CSV file
data.to_csv("student_results.csv", index=False)

print("\nResults saved to student_results.csv")