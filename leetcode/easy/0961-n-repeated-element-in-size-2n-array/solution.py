class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        from collections import Counter
        z=Counter(nums)
        for key,values in z.items():
            w=max(z.values())
            if w==values:
                return key
        