import pandas as pd

print("------ Task 8: Merge, Concatenate, GroupBy & Pivot Table ------")


# --------------------------------------------------
# Dataset 1: Student Information
# --------------------------------------------------

student_info = pd.DataFrame({
    "Student_ID": [101, 102, 103, 104, 105],
    "Name": ["Aryan", "Rahul", "Aman", "Rohit", "Neha"],
    "Course": ["BCA", "BBA", "BCom", "BCA", "BCom"]
})

print("\n------ Student Information ------")
print(student_info)


# --------------------------------------------------
# Dataset 2: Student Performance
# --------------------------------------------------

student_performance = pd.DataFrame({
    "Student_ID": [101, 102, 103, 104, 105],
    "Marks": [89, 82, 91, 76, 88],
    "Attendance": [92, 88, 95, 81, 90]
})

print("\n------ Student Performance ------")
print(student_performance)


# --------------------------------------------------
# 1. MERGE of a DATa
# --------------------------------------------------

merged_data = pd.merge(
    student_info,
    student_performance,
    on="Student_ID"
)

print("\n------ Merged DataFrame ------")
print(merged_data)


# --------------------------------------------------
# 2. CONCATENATE
# --------------------------------------------------

new_students = pd.DataFrame({
    "Student_ID": [106, 107],
    "Name": ["Priya", "Karan"],
    "Course": ["BCA", "BBA"]
})

concatenated_data = pd.concat(
    [student_info, new_students],
    ignore_index=True
)

print("\n------ Concatenated DataFrame ------")
print(concatenated_data)


# --------------------------------------------------
# 3. GROUPBY
# --------------------------------------------------

grouped_data = merged_data.groupby("Course")

print("\n------ GroupBy Course ------")
print(grouped_data["Marks"].mean())


# --------------------------------------------------
# 4. AGGREGATION
# --------------------------------------------------

aggregation_data = merged_data.groupby("Course")["Marks"].agg(
    ["sum", "mean", "count", "min", "max"]
)

print("\n------ Aggregation by Course ------")
print(aggregation_data)


# --------------------------------------------------
# 5. PIVOT TABLE
# --------------------------------------------------

pivot_table = pd.pivot_table(
    merged_data,
    values="Marks",
    index="Course",
    aggfunc=["sum", "mean", "count", "min", "max"]
)

print("\n------ Pivot Table ------")
print(pivot_table)


print("\n------ Task 8 Completed Successfully ------")