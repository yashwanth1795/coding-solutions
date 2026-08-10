class Solution:
    def firstUniqChar(self, s: str) -> int:
        from collections import Counter
        z=Counter(s)
        for key,values in z.items():
            if values==1:
                return s.index(key)
        return -1
        