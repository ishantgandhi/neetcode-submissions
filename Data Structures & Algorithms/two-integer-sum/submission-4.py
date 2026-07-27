class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            val = target - nums[i]
            if nums[i] in dic:
                return [dic[nums[i]],i]
            else:
                dic[val] = i
        