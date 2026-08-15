# JGCFSS01

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Generate 3D array of ones with custom dimensions

Given a function that takes three integers as input: depth, rows, and columns. Modify this function to return a 3D NumPy array filled with ones, with the specified dimensions.

### Sample 1:
Input
Output

```
2 1 3
```

```
[[[1 1 1]]
 [[1 1 1]]]
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-15T03:19:04.390Z  

```py
import numpy as np

def create_3d_ones(depth, rows, columns):
    return np.ones((depth,rows,columns),dtype=int)

# Take depth, rows, and columns as input
d, r, c = map(int, input().split())

# Test the function
result = create_3d_ones(d,r,c)

print(result)

```

---

[View on CodeChef](https://www.codechef.com/problems/JGCFSS01)