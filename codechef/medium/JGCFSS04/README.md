# JGCFSS04

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Extract a cube from within a 3D array

Given a 3D NumPy array of shape (5, 5, 5) filled with random integers from 0 to 99. Extract a cube of size (a, b, c) starting from the position (1, 1, 1) within the array, where a, b, and c are user inputs. Display the extracted cube.
Note that the output may vary for same input.

### Sample 1:
Input
Output

```
3
2
4
```

```
[[[40 59 45 73]
  [84 41 55  3]]
 [[20 22 92 69]
  [25 62 71 57]]
 [[39  4 90 17]
  [90 17 46 94]]]
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-15T03:27:10.269Z  

```py
import numpy as np

# Create a 5x5x5 3D array with random integers from 0 to 99
array_3d = np.random.randint(0, 100, size=(5, 5, 5))

# Get user input for cube dimensions
a = int(input())
b = int(input())
c = int(input())

# Your code here
# Extract the cube from the 3D array
extracted_cube = array_3d[1:1+a, 1:1+b, 1:1+c]
# Print the extracted cube
print(extracted_cube)
```

---

[View on CodeChef](https://www.codechef.com/problems/JGCFSS04)