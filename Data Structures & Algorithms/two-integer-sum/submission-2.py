class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i,n in enumerate(nums):
            a = target - n
            if a in d:
                return [d[a],i]
            d[n] = i
        