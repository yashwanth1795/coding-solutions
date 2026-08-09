# Minimum Total Price After Applying Discounts

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

No description available.

## Solution

**Language:** Python  
**Runtime:** 167 ms (beats 100.00%)  
**Memory:** 35.1 MB (beats 100.00%)  
**Submitted:** 2026-08-09T03:39:09.983Z  

```py
class Solution:
    def minPrice(self, prices: list[int], discounts: list[int]) -> float:
        prices.sort(reverse=True)
        discounts.sort(reverse=True)
        m=0
        for i in range(min(len(prices),len(discounts))):
            w=(prices[i]*(100-discounts[i]))/100
            m=m+w
        for i in range(len(discounts),len(prices)):
            m=m+prices[i]
        return m
```

---

[View on LeetCode](https://leetcode.com/problems/minimum-total-price-after-applying-discounts/)