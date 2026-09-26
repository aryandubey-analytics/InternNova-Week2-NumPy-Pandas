import pandas as pd
import numpy as np

print("================================================")
print("       TASK 10: STUDENT PERFORMANCE ANALYSIS")
print("================================================")


# ------------------------------------------------
# 1. LOAD DTASET---------------------------------
# ------------------------------------------------

df = pd.read_csv("student_performance.csv")

print("\n------ Dataset Loaded Successfully ------")
print(df)


# ------------------------------------------------
# 2. INSPECT DaTASET------------------------------
# ------------------------------------------------

print("\n------ First 5 Rows ------")
print(df.head())

print("\n------ Dataset Shape ------")
print(df.shape)

print("\n------ Column Names ------")
print(df.columns)

print("\n------ Data Types ------")
print(df.dtypes)


# ------------------------------------------------
# 3. CHECK MISSING VALUES-------------------------
# ------------------------------------------------

print("\n------ Missing Values ------")
print(df.isnull().sum())


# ------------------------------------------------
# 4. HANDLE MISSING VALUES------------------------
# ------------------------------------------------

df["Marks"] = df["Marks"].fillna(df["Marks"].mean())
df["Attendance"] = df["Attendance"].fillna(
    df["Attendance"].mean()
)

df["Course"] = df["Course"].fillna(
    df["Course"].mode()[0]
)

print("\n------ Missing Values After Handling ------")
print(df.isnull().sum())


# ------------------------------------------------
# 5. SELECT DATA----------------------------------
# ------------------------------------------------

print("\n------ Name and Marks ------")
print(df[["Name", "Marks"]])


# ------------------------------------------------
# 6. FILTER DATA----------------------------------
# ------------------------------------------------

high_performers = df[df["Marks"] >= 85]

print("\n------ Students Scoring 85 or Above ------")
print(high_performers)


# ------------------------------------------------
# 7. SORT DATA------------------------------------
# ------------------------------------------------

sorted_data = df.sort_values(
    "Marks",
    ascending=False
)

print("\n------ Students Sorted by Marks ------")
print(sorted_data)


# ------------------------------------------------
# 8. GROUPBY--------------------------------------
# ------------------------------------------------

course_analysis = df.groupby("Course")["Marks"].agg(
    ["count", "mean", "min", "max", "sum"]
)

print("\n------ Course-wise Marks Analysis ------")
print(course_analysis)


# ------------------------------------------------
# 9. ATTENDANCE ANALYSIS--------------------------
# ------------------------------------------------

attendance_analysis = df.groupby("Course")["Attendance"].mean()

print("\n------ Average Attendance by Course ------")
print(attendance_analysis)


# ------------------------------------------------
# 10. PIVOT TABLE---------------------------------
# ------------------------------------------------

pivot_table = pd.pivot_table(
    df,
    values="Marks",
    index="Course",
    columns="Gender",
    aggfunc="mean"
)

print("\n------ Pivot Table: Average Marks by Course & Gender ------")
print(pivot_table)


# ------------------------------------------------
# 11. NUMPY ANALYSIS------------------------------
# ------------------------------------------------

average_marks = np.mean(df["Marks"])
highest_marks = np.max(df["Marks"])
lowest_marks = np.min(df["Marks"])

print("\n------ NumPy Statistical Analysis ------")
print("Average Marks:", average_marks)
print("Highest Marks:", highest_marks)
print("Lowest Marks:", lowest_marks)


# ------------------------------------------------
# 12. KEY INSIGHTS-------------------------------
# ------------------------------------------------

top_student = df.loc[df["Marks"].idxmax(), "Name"]

highest_course = (
    df.groupby("Course")["Marks"]
    .mean()
    .idxmax()
)

print("\n------ Key Insights ------")

print("1. Average marks of all students:",
      round(average_marks, 2))

print("2. Highest marks obtained:",
      highest_marks)

print("3. Lowest marks obtained:",
      lowest_marks)

print("4. Top performing student:",
      top_student)

print("5. Course with highest average marks:",
      highest_course)


# ------------------------------------------------
# 13. EXPORT CLEANED DATA-------------------------
# ------------------------------------------------

output_file = "cleaned_student_performance.csv"

df.to_csv(
    output_file,
    index=False
)

print("\n------ Cleaned Dataset Exported ------")
print("File Name:", output_file)


# ------------------------------------------------
# 14. VERIFY EXPORTED DATA------------------------
# ------------------------------------------------

verified_data = pd.read_csv(output_file)

print("\n------ Verified Exported Dataset ------")
print(verified_data)


print("\n================================================")
print("       TASK 10 COMPLETED SUCCESSFULLY")
print("================================================")