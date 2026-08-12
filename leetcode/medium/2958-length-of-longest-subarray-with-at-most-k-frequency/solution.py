class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        z={}
        left=0
        ans=0
        for right in range(len(nums)):
            if nums[right] in z:
                z[nums[right]]+=1
            else:
                z[nums[right]]=1
            while(z[nums[right]]>k):
                z[nums[left]]-=1
                left+=1
            length=right-left+1
            if length>ans:
                ans=length
        return ans
        