class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count = set(nums)
        maxi = 0
        for num in count:
            if num-1 not in count:
                long = 1
                while num + long in count:
                    long += 1
                maxi = max(long,maxi)
        return maxi
