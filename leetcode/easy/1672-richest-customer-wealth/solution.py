class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        z=[]
        for i in accounts:
            m=sum(i)
            z.append(m)
        return max(z)
        