class Solution:
    def minPrice(self, prices: list[int], discounts: list[int]) -> float:
        m=prices[0]
        for i in range(1,len(prices)):
            for j in range(1,len(discounts)):
                w=(prices[i]*(100-discounts[j]))/100
                m=m+w
        
        return m
                
        