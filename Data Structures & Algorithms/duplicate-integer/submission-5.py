class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        new = set()
        for i in range(len(nums)):
            if nums[i] not in new:
                new.add(nums[i])
            else:
                return True
        return False