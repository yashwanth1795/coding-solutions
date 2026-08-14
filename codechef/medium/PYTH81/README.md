# PYTH81

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Problems on Conditional Statements

Listen

Write a program which does the following

- Make an auto-reply program that takes input from the user as an integer variable x
- Compute and output the following to the console Print "Order Confirmed" only if x < 70 else Print "Order Limit reached" In both cases, the program must print "Thank YOU!" on a separate line.
### Sample 1:
Input
Output

```
69
```

```
Order Confirmed
Thank YOU!
```

### Sample 2:
Input
Output

```
70
```

```
Order Limit reached
Thank YOU!
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-14T14:14:16.271Z  

```py
x = int(input())

if (x<70):
    print("Order Confirmed")
else:
    print("Order Limit reached")
print("Thank YOU!")

```

---

[View on CodeChef](https://www.codechef.com/problems/PYTH81)