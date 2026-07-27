class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        dic = {}
        for char in s1:
            if char not in dic:
                dic[char] = 1
            else:
                dic[char]+=1
        
        l = 0
        r = len(s1)
        while r <= len(s2):
            window = s2[l:r]
            Wdic={}
            for char in window:
                if char not in Wdic:
                    Wdic[char] = 1
                else:
                    Wdic[char]+=1
            if Wdic == dic:
                return True
            l+=1
            r+=1
        return False