class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        h1 = {}
        h2 = {}
        for si in s:
            if si not in h1:
                h1[si] = 1
            else:
                h1[si]+=1
        for ti in t:
            if ti not in h2:
                h2[ti]=1
            else:
                h2[ti]+=1
        return h1==h2