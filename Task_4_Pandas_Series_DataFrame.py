import pandas as pd

print("------ Pandas Series & DataFrame ------")

# Create a Pandas Series
student_names = pd.Series(["Aryan", "Rahul", "Aman", "Rohit", "Neha"])

print("\n------ Pandas Series ------")
print(student_names)


# Create a DataFrame: Creating a Data Frame
student_data = {
    "Name": ["Aryan", "Rahul", "Aman", "Rohit", "Neha"],
    "Age": [19, 20, 18, 21, 19],
    "Course": ["BCA", "BBA", "B.Com", "BCA", "B.Com"]
}

df = pd.DataFrame(student_data)

print("\n------ Original DataFrame ------")
print(df)


# Display column names
print("\n------ Column Names ------")
print(df.columns)


# Display index
print("\n------ Index ------")
print(df.index)


# Add a new column : Adding a new column Marks.
df["Marks"] = [89, 82, 91, 76, 88]

print("\n------ Updated DataFrame ------")
print(df)