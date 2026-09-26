import pandas as pd

print("------ Selecting, Filtering & Sorting Data ------")

data = {
    "Name": ["Aryan", "Rahul", "Aman", "Rohit", "Neha",
             "Priya", "Karan", "Sneha", "Vikas", "Anjali"],
    "Age": [19, 20, 18, 21, 19, 20, 19, 18, 21, 20],
    "Course": ["BCA", "BBA", "BCom", "BCA", "BCom",
               "BCA", "BBA", "BCom", "BCA", "BBA"],
    "Marks": [89, 82, 91, 76, 88, 94, 79, 86, 73, 90],
    "Attendance": [92, 88, 95, 81, 90, 97, 84, 91, 78, 93]
}

df = pd.DataFrame(data)

print("\n------ Original DataFrame ------")
print(df)



print("\n------ Marks Column ------")
print(df["Marks"])



print("\n------ Name and Marks ------")
print(df[["Name", "Marks"]])



print("\n------ Students with Marks Greater Than 85 ------")
high_marks = df[df["Marks"] > 85]
print(high_marks)



print("\n------ Students with Attendance Greater Than 90 ------")
high_attendance = df[df["Attendance"] > 90]
print(high_attendance)



print("\n------ BCA Students ------")
bca_students = df[df["Course"] == "BCA"]
print(bca_students)



print("\n------ Sorted by Marks (Ascending) ------")
print(df.sort_values("Marks"))

 
print("\n------ Sorted by Marks (Descending) ------")
print(df.sort_values("Marks", ascending=False))