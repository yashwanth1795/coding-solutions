# PYTH80

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Multiple Choice Question

What will be the output of this code?

```
a = 0
b = 0

if a >= b:
   print("a is greater or equal to b.")
if (a == 0) or (b == 0):
   print("At least one is 0.")
if (a == 0) and (b == 0):
   print("Both are 0.")
print("Program ends")

```

## Solution

**Language:** C++  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-14T14:12:53.947Z  

```cpp
# The following helps accept multiple user input
z, x, c = map(int, input().split())
if (c>x or c>z):
    print("PASS")
else:
    print("FAIL")
```

---

[View on CodeChef](https://www.codechef.com/problems/PYTH80)