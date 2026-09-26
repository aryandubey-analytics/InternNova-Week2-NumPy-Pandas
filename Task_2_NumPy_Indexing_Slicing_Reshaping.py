import numpy as np

print("------ Numpy Indexing, Slicing & Reshaping ------ ")

print("\n--- One Dimensional Numpy Array ---")
array_1d = np.array([10,20,30,40,50,60,70,80,90,100,110,120])

print("\nOrigional 1D Array:") # One dimension array 
print(array_1d)

print("\n------ Indexing ------") # Indexing of element 
print("First Element:", array_1d[0])
print("Fifth Element:", array_1d[4])
print("Last Element:", array_1d[-1])


print("\n ------ Slicing ------") # Slicing of Element
print("Elements from index 2 to 6:", array_1d[2:7])
print("First 5 Elements:", array_1d[:5])
print("Elements from index 5 onwards:", array_1d[5:])

# Two Dimension Array
array_2d = np.array([
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 100, 110, 120]
])

print("\n------ Two Dimensional Array ------")
print(array_2d)

print("\n------ Acessing Rows and Columns -------")
print("\nFirst Row:")
print(array_2d[0])

print("\nSecond Column:")
print(array_2d[:, 1])

print("\nElement at Row 2, Column 3:")
print(array_2d[1, 2])


print("\n------ Reshaping Origional Array ------")
reshaped_array = array_1d.reshape(4, 3)

print("\n------ Original Array ------")
print(array_1d)

print("\n------ Reshaped Array (4 x 3) ------")
print(reshaped_array)