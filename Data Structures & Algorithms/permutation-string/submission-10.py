class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1A = [0]*26
        s2A = [0]*26
        for char in s1:
            s1A[ord(char)-ord('a')]+=1
        if len(s1) > len(s2):
            return False
        l = 0
        r = len(s1)
        for char in s2[l:r]:
            s2A[ord(char)-ord('a')]+=1
        while r < len(s2):
            if s1A == s2A:
                return True
            else:
                s2A[ord(s2[l])-ord('a')]-=1 
                l+=1
                s2A[ord(s2[r])-ord('a')]+=1 
                r+=1
        if s1A == s2A:
                return True
        return False
                

