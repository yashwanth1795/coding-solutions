# PYTH77

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Or Statement

Listen

The  **`OR`**  operator is another logical operator in Python that allows you to combine multiple conditions.
It returns  **TRUE**  if at least one of the conditions is true, and  **False**  if all the conditions are false.

Suppose you have a variable age that represents a person's age, and you want to check if the age is either less than 18 or greater than 65.

```
age = 22

if age < 18 or age > 65:
    print("This person is either under 18 or over 65.")
else:
    print("This person is between 18 and 65.")

# Output
# This person is between 18 and 65.

```

### Task

Write a program which does the following

- Take input from the console for integer variables z, x and c.
- Compute and output the following for each tuple z, x and c "PASS" if c is greater than either x or z Otherwise print "FAIL" in every other case
### Sample 1:
Input
Output

```
5 3 2
```

```
FAIL
```

### Sample 2:
Input
Output

```
5 10 8
```

```
PASS
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-14T14:11:09.298Z  

```py
# The following helps accept multiple user input
z, x, c = map(int, input().split())
if (c>x or c>z):
    print("PASS")
else:
    print("FAIL")
```

---

[View on CodeChef](https://www.codechef.com/problems/PYTH77)