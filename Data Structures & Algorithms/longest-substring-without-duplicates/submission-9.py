class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        l = 0
        r = 0
        res = 0
        temp = 0
        while r < len(s):
            if s[r] not in seen:
                seen.add(s[r])
                temp += 1
                r+=1
            else:
                seen.remove(s[l])
                l+=1
                temp-=1
            res = max(temp,res)
        return res
                