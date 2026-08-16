# 3Sum

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given an integer array nums, return all the triplets `[nums[i], nums[j], nums[k]]` such that `i != j`, `i != k`, and `j != k`, and `nums[i] + nums[j] + nums[k] == 0`.

Notice that the solution set must not contain duplicate triplets.

 

 **Example 1:** 

```
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

```

 **Example 2:** 

```
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

```

 **Example 3:** 

```
Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.

```

 

 **Constraints:** 

- 3 <= nums.length <= 3000
- -105 <= nums[i] <= 105

## Solution

**Language:** Python  
**Runtime:** 1662 ms (beats 7.89%)  
**Memory:** 216.4 MB (beats 5.36%)  
**Submitted:** 2026-08-16T04:07:17.549Z  

```py
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        s=[]
        for i in range(len(nums)):
            j=i+1
            k=len(nums)-1
            while(j<k):
                total=nums[i]+nums[j]+nums[k]

                if total==0:
                    s.append((nums[i],nums[j],nums[k]))
                    j+=1
                    k-=1
                elif total<0:
                    j+=1
                else:
                    k-=1
        return [list(x) for x in set(s)]
       
       
```

---

[View on LeetCode](https://leetcode.com/problems/3sum/)