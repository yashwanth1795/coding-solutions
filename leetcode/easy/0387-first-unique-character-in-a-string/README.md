# First Unique Character in a String

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given a string `s`, find the  **first**  non-repeating character in it and return its index. If it  **does not**  exist, return `-1`.

 

 **Example 1:** 

 **Input:**  s = "leetcode"

 **Output:**  0

 **Explanation:** 

The character `'l'` at index 0 is the first character that does not occur at any other index.

 **Example 2:** 

 **Input:**  s = "loveleetcode"

 **Output:**  2

 **Example 3:** 

 **Input:**  s = "aabb"

 **Output:**  -1

 

 **Constraints:** 

- 1 <= s.length <= 105
- s consists of only lowercase English letters.

## Solution

**Language:** Python  
**Runtime:** 23 ms (beats 99.33%)  
**Memory:** 19.9 MB (beats 6.67%)  
**Submitted:** 2026-08-10T02:25:30.581Z  

```py
class Solution:
    def firstUniqChar(self, s: str) -> int:
        from collections import Counter
        z=Counter(s)
        for key,values in z.items():
            if values==1:
                return s.index(key)
        return -1
        
```

---

[View on LeetCode](https://leetcode.com/problems/first-unique-character-in-a-string/)