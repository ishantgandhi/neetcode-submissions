class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub = set()
        l = 0
        r = 0
        curr = 0
        longest = 0
        while r < len(s):
            if s[r] not in sub:
                sub.add(s[r])
                curr+=1
                r+=1
            else:
                sub.remove(s[l])
                curr-=1
                l+=1
            longest = max(curr,longest)
        return longest