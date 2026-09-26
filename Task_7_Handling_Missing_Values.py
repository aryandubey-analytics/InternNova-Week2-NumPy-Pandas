import pandas as pd
import numpy as np

print("------ Task 7: Handling Missing Values ------")

# Create a dataset containing missing values
data = {
    "Name": ["Aryan", "Rahul", "Aman", "Rohit", "Neha", "Priya"],
    "Age": [19, 20, np.nan, 21, 19, 20],
    "Course": ["BCA", "BBA", "BCom", "BCA", np.nan, "BCA"],
    "Marks": [89, np.nan, 91, 76, 88, np.nan],
    "Attendance": [92, 88, 95, np.nan, 90, 97]
}

df = pd.DataFrame(data)

# Display original dataset
print("\n------ Dataset Before Handling Missing Values ------")
print(df)

# Identify missing values
print("\n------ Missing Values (isnull) ------")
print(df.isnull())

# Count missing values in each column
print("\n------ Missing Values Count ------")
print(df.isnull().sum())

# Remove rows containing missing values
df_removed = df.dropna()

print("\n------ Dataset After Removing Rows with Missing Values ------")
print(df_removed)

# Fill missing numerical values with column mean
df_filled = df.copy()

df_filled["Age"] = df_filled["Age"].fillna(df_filled["Age"].mean())
df_filled["Marks"] = df_filled["Marks"].fillna(df_filled["Marks"].mean())
df_filled["Attendance"] = df_filled["Attendance"].fillna(
    df_filled["Attendance"].mean()
)

# Fill missing categorical value with mode
df_filled["Course"] = df_filled["Course"].fillna(
    df_filled["Course"].mode()[0]
)

print("\n------ Dataset After Filling Missing Values ------")
print(df_filled)

# Final missing-value check
print("\n------ Final Missing Values Count ------")
print(df_filled.isna().sum())

print("\n------ Why Handling Missing Data Is Important ------")
print(
    "Handling missing data is important because missing values can "
    "affect calculations, reduce data quality, and lead to inaccurate "
    "analysis. Properly handling missing values helps produce more "
    "reliable and meaningful analytical results."
)