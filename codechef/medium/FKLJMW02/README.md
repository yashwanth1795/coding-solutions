# FKLJMW02

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Random Dice Roll Simulator

Create a program that simulates rolling a six-sided die multiple times. You are given number of times the die rolls.
Write a program that use NumPy's `randint` function to generate random numbers between 1 and 6 (inclusive) to represent the die rolls. Display the results as a NumPy array. Note that the output may vary for same input.

### Sample 1:
Input
Output

```
3
```

```
[4 6 3]
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-13T14:23:03.001Z  

```py
import numpy as np

# Ask the user for the number of rolls
num_rolls = int(input())

# Create a NumPy array of random dice rolls
dice_rolls =np.random.randint(1,7,size=num_rolls)

# Print the resulting array
print(dice_rolls)

```

---

[View on CodeChef](https://www.codechef.com/problems/FKLJMW02)