# Container With Most Water

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

You are given an integer array `height` of length `n`. There are `n` vertical lines drawn such that the two endpoints of the `ith` line are `(i, 0)` and `(i, height[i])`.

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return  *the maximum amount of water a container can store*.

 **Notice**  that you may not slant the container.

 

 **Example 1:** 

```
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

```

 **Example 2:** 

```
Input: height = [1,1]
Output: 1

```

 

 **Constraints:** 

- n == height.length
- 2 <= n <= 105
- 0 <= height[i] <= 104

## Solution

**Language:** Python  
**Runtime:** 62 ms (beats 30.27%)  
**Memory:** 29.7 MB (beats 37.62%)  
**Submitted:** 2026-08-15T02:53:52.146Z  

```py
class Solution:
    def maxArea(self, height: List[int]) -> int:
        i=0
        j=len(height)-1
        max_water=0
        while(i<j):
            z=min(height[i],height[j])
            width=j-i
            water=width*z
            max_water=max(max_water,water)
            if height[i]<height[j]:
                i+=1
            else:
                j-=1
        return max_water
            


        
```

---

[View on LeetCode](https://leetcode.com/problems/container-with-most-water/)