class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        count = 0
        res = 0
        l = 0
        r = 0
        while r < len(s):
            if s[r] not in seen:
                count+=1
                seen.add(s[r])
                r+=1
            else:
                seen.remove(s[l])
                l+=1
                count-=1
            res = max(count,res)
        return res
        