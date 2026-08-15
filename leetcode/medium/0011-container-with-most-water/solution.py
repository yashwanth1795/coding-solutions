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
            


        