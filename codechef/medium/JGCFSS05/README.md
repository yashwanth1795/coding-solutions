# JGCFSS05

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

_Description not available._

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-15T03:27:11.008Z  

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

[View on CodeChef](https://www.codechef.com/problems/JGCFSS05)