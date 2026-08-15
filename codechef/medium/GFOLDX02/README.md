# GFOLDX02

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

_Description not available._

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-15T03:04:27.856Z  

```py
import numpy as np

# Get input from the user and convert it into numpy array of integers
input_list = input().split()
input_array = np.array(input_list, dtype=int)
result=input_array[::3]


print(result)

```

---

[View on CodeChef](https://www.codechef.com/problems/GFOLDX02)