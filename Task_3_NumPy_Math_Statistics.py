import numpy as np  # Importing numpy as np

print("------ NumPy Mathematical & Statistical Operations ------")

# Data Set
data = np.array([10, 25, 30, 40, 50])

print("\nOriginal Function Data:")
print(data)

print("\n------ Mathematical Operations ------")

print("Addition by 9:", data + 9)
print("Subtraction by 5:", data - 5)
print("Multiplication by 2:", data * 2)
print("Division by 2:", data / 2)


print("\n------ Statistical Operations ------")

print("Mean:", np.mean(data))
print("Median:", np.median(data))
print("Minimum:", np.min(data))
print("Maximum:", np.max(data))
print("Standard Deviation:", np.std(data))
print("Sum:", np.sum(data))