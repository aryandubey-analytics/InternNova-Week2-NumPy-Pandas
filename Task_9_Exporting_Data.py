import pandas as pd

print("------ Task 9: Exporting Data ------")




#-------------------------------
#--------Data Set---------------
#-------------------------------
data = {
    "Name": ["Aryan", "Rahul", "Aman", "Rohit", "Neha"],
    "Age": [19, 20, 18, 21, 19],
    "Course": ["BCA", "BBA", "BCom", "BCA", "BCom"],
    "Marks": [89, 82, 91, 76, 88],
    "Attendance": [92, 88, 95, 81, 90]
}

df = pd.DataFrame(data)

print("\n------ Processed DataFrame ------")
print(df)


output_file = "processed_students_data.csv"

df.to_csv(output_file, index=False)# Changing to csv

print("\n------ Data Exported Successfully ------")
print("File Name:", output_file)



verified_data = pd.read_csv(output_file)

print("\n------ Verified Exported Data ------")
print(verified_data)


print("\n------ Task 9 Completed Successfully ------")