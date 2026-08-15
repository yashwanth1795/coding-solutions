import numpy as np

# Get user input for dimensions
depth = int(input())
rows = int(input())
cols = int(input())

# Get user input for array elements
elements = input().split()
elements = [int(x) for x in elements]
arr_1d=np.array(elements)
reshaped_arr=arr_1d.reshape(depth,rows,cols)


# Your code to reshape the 1D array into a 3D array goes here

# Print the reshaped array
print(reshaped_arr)
