# FKLJMW01

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Create NumPy array from exam scores

You are a teacher who wants to analyze student exam scores. You have a list of scores and want to convert it into a NumPy array for further analysis. Write a Python program that takes a list of exam scores as input and creates a NumPy array from it.

### Sample 1:
Input
Output

```
4 3 5 6 7
```

```
[4 3 5 6 7]
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-13T14:20:11.198Z  

```py
import numpy as np

# Get the list of exam scores from the user
exam_scores = input().split()

# Convert the input strings to integers
exam_scores = [int(score) for score in exam_scores]

# Create a NumPy array from the list of exam scores
# Your code here
exam_scores_array = np.array(exam_scores)

# Print the resulting NumPy array
print(exam_scores_array)
```

---

[View on CodeChef](https://www.codechef.com/problems/FKLJMW01)