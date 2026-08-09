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