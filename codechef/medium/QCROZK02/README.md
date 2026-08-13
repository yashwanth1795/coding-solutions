# QCROZK02

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

_Description not available._

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-13T14:33:06.282Z  

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

[View on CodeChef](https://www.codechef.com/problems/QCROZK02)