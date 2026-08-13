# FKLJMW03

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Generate a sequence of odd numbers

Create a NumPy array containing a sequence of odd numbers from a given start value to an end value. The user should input the start and end values, and the program should generate the array of odd numbers within that range.

### Sample 1:
Input
Output

```
4
9
```

```
[5 7 9]
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-13T14:25:05.367Z  

```py
import numpy as np

start = int(input())
end = int(input())

# Create a NumPy array of odd numbers from start to end
odd_numbers = np.arange(start+(start%2==0),end+1,2)

# Print array of odd numbers
print(odd_numbers)

```

---

[View on CodeChef](https://www.codechef.com/problems/FKLJMW03)