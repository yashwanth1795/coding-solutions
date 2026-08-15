# GFOLDX03

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Mask negative numbers in a NumPy array

Create a NumPy array from user input and create a boolean mask to filter out negative numbers. Then, use this mask to display only the non-negative numbers from the original array.

### Sample 1:
Input
Output

```
13 -11 8 7 -4 0 2
```

```
[13  8  7  0  2]
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-15T03:08:32.094Z  

```py
import numpy as np

# Get user input
input_string = input()
numbers = [int(x) for x in input_string.split()]

# Create a NumPy array
arr = np.array(numbers)
mask=arr>=0
result=arr[mask]
print( result)
```

---

[View on CodeChef](https://www.codechef.com/problems/GFOLDX03)