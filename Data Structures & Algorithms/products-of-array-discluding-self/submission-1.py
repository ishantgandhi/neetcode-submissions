class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)
        pre = suf = 1

        for num in range(len(nums)):
            result[num] = pre
            pre *= nums[num]
        
        for num in range(len(nums) - 1,-1,-1):
            result[num]*=suf
            suf*=nums[num]
        
        return result