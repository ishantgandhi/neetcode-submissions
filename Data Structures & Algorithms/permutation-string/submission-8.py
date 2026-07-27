class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0 
        r = len(s1)
        if len(s1) > len(s2):
            return False
        while r <= len(s2):
            if "".join(sorted(s1) ) == "".join(sorted(s2[l:r])):
                return True
            else:
                l+=1
                r+=1
        return False