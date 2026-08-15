# GFOLDX03

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Reverse a NumPy array using slicing

In this practice problem, you will learn how to reverse a NumPy array using array slicing. You'll be given a NumPy array, and your task is to reverse the order of its elements using slicing operations.

### Sample 1:
Input
Output

```
9 14 20 7 3 5
```

```
[ 5  3  7 20 14  9]
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-15T03:05:03.119Z  

```py
import numpy as np

# Create a NumPy array from user input
input_list = input().split()
input_list = [int(score) for score in input_list]
arr = np.array(input_list)

reversed_arr=arr[::-1]

print(reversed_arr)
```

---

[View on CodeChef](https://www.codechef.com/problems/GFOLDX03)