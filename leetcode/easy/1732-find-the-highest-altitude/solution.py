class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        at=0
        hi=0
        for i in gain:
            at=at+i
            if at>hi:
                hi=at
        return (hi)
        