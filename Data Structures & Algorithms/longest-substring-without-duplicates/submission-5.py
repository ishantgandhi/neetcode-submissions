class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        curr = 0
        res = 0
        l,r = 0,0
        while r < len(s):
            if s[r] not in seen:
                curr += 1
                seen.add(s[r])
                r+=1
            else:
                seen.remove(s[l])
                curr-=1
                l+=1
            res = max(res,curr)
        return res
