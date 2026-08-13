class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        z=str(n)
        p=1
        s=0
        for i in z:
            p=p*int(i)
            s=s+int(i)
        return p-s
        
    

        