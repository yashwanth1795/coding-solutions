# GFOLDX01

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Extract every third element from an array

Create a NumPy array from a list of integers provided by the user. Then, extract every third element from this array starting from the first element (index 0). Use array indexing to accomplish this task.

### Sample 1:
Input
Output

```
4 6 -7 0 3 8
```

```
[4 0]
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-15T03:04:27.065Z  

```py
import numpy as np

# Get input from the user and convert it into numpy array of integers
input_list = input().split()
input_array = np.array(input_list, dtype=int)
result=input_array[::3]


print(result)

```

---

[View on CodeChef](https://www.codechef.com/problems/GFOLDX01)