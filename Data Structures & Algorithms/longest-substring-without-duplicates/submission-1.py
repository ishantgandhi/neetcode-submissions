class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r,curr = 0,0,0
        sub = []
        ans = 0
        while r < len(s):
            if s[r] not in sub:
                sub.append(s[r])
                curr+=1
                ans=max(ans,curr)
                r+=1
            else:
                sub.remove(s[l])
                l+=1
                curr-=1
        return ans
