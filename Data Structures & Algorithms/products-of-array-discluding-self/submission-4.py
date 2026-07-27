class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]*len(nums)
        pre = suf = 1
        for num in range(len(nums)):
            res[num] = pre
            pre*=nums[num]
        for num in range(len(nums)-1,-1,-1):
            res[num] *= suf
            suf*= nums[num]
        return res
