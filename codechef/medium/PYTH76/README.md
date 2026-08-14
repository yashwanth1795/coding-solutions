# PYTH76

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### And Statement

Listen

Till now we used only one condition in our  **if**  or  **elif**  statements.
But what if we want to use multiple conditions?
Say we want to check if a person is female and older than 18 years of age, how can we do that in Python?

In Python, the  **`AND`**  operator is a logical operator that allows you to combine multiple conditions.
It returns  **TRUE**  if all the conditions are true, and  **FALSE**  if at least one condition is false.

Let's start with a simple example.
Imagine you have two variables:  **`x`**  and  **`y`**.
You want to check if both  **`x`**  is greater than 5 and  **`y`**  is less than 10.
Here's how you would use the  **`and`**  operator to combine these conditions:

```
x = 8
y = 7

if x > 5 and y < 10:
    print("Both conditions are true!")
else:
    print("At least one condition is false.")

# For the given values of x and y, the above program will return "Both conditions are true!".

```

### Task

Write a program which does the following:

- Declare a variable a and initialize it to the values $15$
- Compute if a is completely divisible by both 7 and 5
- Depending on the result above - output the following to the console The number is divisible by both 5 & 7 The number is not divisible by both 5 & 7

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-14T14:07:28.242Z  

```py
# Update the code below to solve the problem

a = 15

# a%7 returns the remainder when a is divided by 7
if (a%7 == 0) and (a%5 == 0):       
    print("The number is divisble both 5 & 7")
else:
    print("The number is not divisible by both 5 & 7")
```

---

[View on CodeChef](https://www.codechef.com/problems/PYTH76)