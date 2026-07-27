class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1]*len(nums)
        prefix = suffix = 1

        for num in range(len(nums)):
            result[num] = prefix
            prefix *= nums[num]
        
        for num in range(len(nums) - 1,-1,-1):
            result[num] *= suffix
            suffix *= nums[num]

        return result