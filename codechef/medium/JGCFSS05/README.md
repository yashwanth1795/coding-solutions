# JGCFSS05

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Extract specific rows from all layers of 3D array

In this task, you will create a 3D NumPy array and extract specific rows from all layers of the array. You'll be given the dimensions of the array and the row numbers to extract. Your goal is to create the array, fill it with sequential numbers, and then extract the specified rows from each layer.

### Sample 1:
Input
Output

```
3
3
2
1 2
```

```
[[[ 2  3]
  [ 4  5]]
 [[ 8  9]
  [10 11]]
 [[14 15]
  [16 17]]]
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-15T03:28:21.982Z  

```py
import numpy as np

def extract_rows_from_layers(depth, rows, cols, row_indices):
    # Create a 3D array with the given dimensions
    array_3d = np.arange(depth * rows * cols).reshape(depth, rows, cols)
    # Your code here to extract the specified rows from all layers
    result = array_3d[:, row_indices, :]
    
    return result

# Take depth of the 3D array as input 
depth = int(input())

# Take number of rows as input
rows = int(input())

# Take number of columns as input
cols = int(input())

# Take row_indices to extract as input
row_indices = list(map(int, input().split()))

# Call the function and print the result
result = extract_rows_from_layers(depth, rows, cols, row_indices)
print(result)

```

---

[View on CodeChef](https://www.codechef.com/problems/JGCFSS05)