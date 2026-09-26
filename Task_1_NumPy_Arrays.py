import numpy as np 

print("------ Numpy Introduction & Arrays ------")
print("\n------ One Dimensional Array ------")
array_1d = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 110]) #One Dimension Array

print("Array:", array_1d)
print("Shape:", array_1d.shape)
print("Size:", array_1d.size)
print("Data Type:", array_1d.dtype)

print("\n------ Two Dimensional Array ------ ")
array_2d = np.array([
    [10, 20, 30, 40, 50],
    [60, 70, 80, 90, 100]
])

print("Array:", array_2d)
print("Shape:", array_2d.shape)
print("Size:", array_2d.size)
print("Data Type:", array_2d.dtype)