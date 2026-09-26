import pandas as pd

print("------ Reading & Inspecting Data ------")


df = pd.read_csv("students_data.csv")


print("\n------ First 5 Rows ------")
print(df.head())

print("\n------ Last 5 Rows ------")
print(df.tail())


print("\n------ Shape of Dataset ------")
print("Rows and Columns:", df.shape)


print("\n------ Column Names ------")
print(df.columns)


print("\n------ Data Types ------")
print(df.dtypes)


print("\n------ Dataset Information ------")
df.info()


print("\n------ Statistical Summary ------")
print(df.describe())