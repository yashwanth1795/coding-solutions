# Majority Element

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given an array `nums` of size `n`, return  *the majority element*.

The majority element is the element that appears more than `⌊n / 2⌋` times. You may assume that the majority element always exists in the array.

 

 **Example 1:** 

```
Input: nums = [3,2,3]
Output: 3

```

 **Example 2:** 

```
Input: nums = [2,2,1,1,1,2,2]
Output: 2

```

 

 **Constraints:** 

- n == nums.length
- 1 <= n <= 5 * 104
- -109 <= nums[i] <= 109
- The input is generated such that a majority element will exist in the array.

 

 **Follow-up:**  Could you solve the problem in linear time and in `O(1)` space?

## Solution

**Language:** Python  
**Runtime:** 3 ms (beats 84.70%)  
**Memory:** 21.1 MB (beats 84.27%)  
**Submitted:** 2026-08-10T02:29:23.126Z  

```py
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        from collections import Counter
        z=Counter(nums)
        for key, values in z.items():
            w=max(z.values())
            if values==w:
                return key
        
```

---

[View on LeetCode](https://leetcode.com/problems/majority-element/)