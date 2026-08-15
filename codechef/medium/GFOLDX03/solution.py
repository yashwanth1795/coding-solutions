import numpy as np

# Get user input
input_string = input()
numbers = [int(x) for x in input_string.split()]

# Create a NumPy array
arr = np.array(numbers)
mask=arr>=0
result=arr[mask]
print( result)