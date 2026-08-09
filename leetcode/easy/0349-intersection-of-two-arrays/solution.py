class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        z=[]
        for i in nums2:
            if i in nums1:
                z.append(i)
            
        return list(set(z))
       
        