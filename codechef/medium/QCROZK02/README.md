# QCROZK02

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Convert numeric scores to letter grades

Given a NumPy program that takes a list of integer test scores. You have to complete `convert_to_grades` where it converts the test_scores into an array of letter grade strings. Use the following grading scale:
90-100: 'A'
80-89: 'B'
70-79: 'C'
60-69: 'D'
0-59: 'F'

### Sample 1:
Input
Output

```
73 84 91 78 85 67
```

```
['C' 'B' 'A' 'C' 'B' 'D']
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-13T14:39:00.948Z  

```py
import numpy as np

def convert_to_grades(scores):
    # Create a NumPy array from the input list
    score_array = np.array(scores)
    
    # Create an empty string array of the same shape as score_array
    grade_array = np.empty_like(score_array, dtype='U1')
    grade_array[score_array>=90]='A'
    grade_array[(score_array>=80) & (score_array<=89)]='B'
    grade_array[(score_array>=70) & (score_array<=79)]='C'
    grade_array[(score_array>=60) & (score_array<=69)]='D'
    grade_array[score_array<60]='F'
    

    
    return grade_array

# Get input from user
scores = input().split()
scores = [int(score) for score in scores]

# we can also use map to take input: scores = list(map(int, input().split()))

# Call the function and print the result
result = convert_to_grades(scores)
print(result)

```

---

[View on CodeChef](https://www.codechef.com/problems/QCROZK02)