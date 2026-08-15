# JGCFSS02

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Reshape array to user specs

Given a program that takes user input for the dimensions of a 3D array (depth, rows, columns) and a list of integers. Make this program to reshape a 1D NumPy array created from the input list into a 3D array with the specified dimensions.

### Sample 1:
Input
Output

```
3
2
3
9 11 17 5 6 14 8 21 9 5 16 18 26 3 45 28 7 13
```

```
[[[ 9 11 17]
  [ 5  6 14]]
 [[ 8 21  9]
  [ 5 16 18]]
 [[26  3 45]
  [28  7 13]]]
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-15T03:22:08.983Z  

```py
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

```

---

[View on CodeChef](https://www.codechef.com/problems/JGCFSS02)