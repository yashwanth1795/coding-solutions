# JGCFSS03

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Chessboard Square Extractor

Given a program that simulates a chessboard using a 2D NumPy array. The chessboard to be an 8x8 grid where 0 represents white squares and 1 represents black squares. The program take two user inputs, 'a' and 'b', representing the row and column of a square on the chessboard. Your task is to extract and display a 3x3 subgrid centered on the selected square.

### Sample 1:
Input
Output

```
4
5
```

```
[[1 0 1]
 [0 1 0]
 [1 0 1]]
```

### Explanation:

0 1 0 1 0 1 0 1
1 0 1 0 1 0 1 0
0 1 0 1 0 1 0 1
1 0 1 0  **1 0 1**  0
0 1 0 1  **0 1 0**  1
1 0 1 0  **1 0 1**  0
0 1 0 1 0 1 0 1
1 0 1 0 1 0 1 0

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-15T03:26:03.025Z  

```py
import numpy as np

# Create the chessboard
chessboard = np.zeros((8, 8), dtype=int)
chessboard[1::2, 0::2] = 1
chessboard[0::2, 1::2] = 1

# Take row number(0-7) as input
a = int(input())

# Take column number(0-7) as input
b = int(input())

# Your code here
# Extract the 3x3 subgrid

# Print the result
row_start = max(0, a - 1)
row_end = min(8, a + 2)
col_start = max(0, b - 1)
col_end = min(8, b + 2)
subgrid = chessboard[row_start:row_end, col_start:col_end]

# Print the result
print(subgrid)
```

---

[View on CodeChef](https://www.codechef.com/problems/JGCFSS03)