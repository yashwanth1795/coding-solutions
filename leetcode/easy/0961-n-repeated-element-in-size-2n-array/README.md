# N-Repeated Element in Size 2N Array

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

You are given an integer array `nums` with the following properties:

- nums.length == 2 * n.
- nums contains n + 1 unique values, n of which occur exactly once in the array.
- Exactly one element of nums is repeated n times.

Return  *the element that is repeated* `n` *times*.

 

 **Example 1:** 

```
Input: nums = [1,2,3,3]
Output: 3

```

 **Example 2:** 

```
Input: nums = [2,1,2,5,3,2]
Output: 2

```

 **Example 3:** 

```
Input: nums = [5,1,5,2,5,3,5,4]
Output: 5

```

 

 **Constraints:** 

- 2 <= n <= 5000
- nums.length == 2 * n
- 0 <= nums[i] <= 104
- nums contains n + 1 unique elements and one of them is repeated exactly n times.

## Solution

**Language:** Python  
**Runtime:** 6 ms (beats 35.36%)  
**Memory:** 20.5 MB (beats 30.61%)  
**Submitted:** 2026-08-10T02:20:29.826Z  

```py
class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        from collections import Counter
        z=Counter(nums)
        for key,values in z.items():
            w=max(z.values())
            if w==values:
                return key
        
```

---

[View on LeetCode](https://leetcode.com/problems/n-repeated-element-in-size-2n-array/)