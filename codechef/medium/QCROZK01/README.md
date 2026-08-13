# QCROZK01

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Even Number Boolean Mapper

You are given an incomplete NumPy program which takes a list of integers as input. Your task is to complete that such that it returns a boolean array where True represents even numbers and False represents odd numbers.

### Sample 1:
Input
Output

```
9 14 22 17 5
```

```
[False  True  True False False]
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-13T14:33:05.014Z  

```py
import numpy as np

def even_number_mapper(numbers):
    # Convert the input list to a NumPy array
    arr = np.array(numbers)
    
    even_mask=arr%2==0
    return even_mask

# Get input from the user
input_numbers = input().split()
numbers_list = [int(num) for num in input_numbers]

# Call the function and print the result
result = even_number_mapper(numbers_list)
print(result)
```

---

[View on CodeChef](https://www.codechef.com/problems/QCROZK01)