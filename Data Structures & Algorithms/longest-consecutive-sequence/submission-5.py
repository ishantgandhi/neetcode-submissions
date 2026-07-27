class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        found = set(nums)
        res = 0
        for num in nums:
            if num-1 not in found:
                l=1
                while num+l in found:
                    l+=1
                res = max(l,res)
        return res