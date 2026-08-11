class Solution:
    def hammingWeight(self, n: int) -> int:
        z=[]
        while(n>0):
            r=n%2
            z.append(r)
            n=n//2
        c=0
        for i in z:
            if i==1:
                c+=1
        return c



        