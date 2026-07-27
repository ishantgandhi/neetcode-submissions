class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r,curr,longest = 0,0,0,0
        sub = []
        while r < len(s):
            if s[r] not in sub:
                sub.append(s[r])
                curr+=1
                r+=1
            else:
                sub.remove(s[l])
                l+=1
                curr-=1
            longest = max(curr,longest)
        return longest