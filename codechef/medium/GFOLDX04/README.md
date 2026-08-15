# GFOLDX04

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Filter temperatures above 50 and even numbers

Create a NumPy array of temperatures and use Boolean indexing to extract all even temperatures above 50°F. This task will help you practice Boolean indexing and conditional filtering on NumPy arrays.

### Sample 1:
Input
Output

```
34 42 50 47 57 54 60 21
```

```
[54 60]
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-15T03:11:13.725Z  

```py
import numpy as np

# Get temperature data from user input
temperatures = input().split()
temperatures = [int(score) for score in temperatures]
temp_array = np.array(temperatures)

filtered_temps=temp_array[(temp_array>50 )&(temp_array%2==0)]
print(filtered_temps)

```

---

[View on CodeChef](https://www.codechef.com/problems/GFOLDX04)