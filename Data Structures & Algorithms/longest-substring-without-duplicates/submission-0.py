class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = j = curr = 0
        ans = 0
        sub = []
        while j < len(s):
            if s[j] not in sub:
                sub.append(s[j])
                curr += 1
                ans = max(ans, curr)
                j += 1
            else:
                sub.remove(s[i])
                i += 1
                curr -= 1
        return ans
                
