class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        valid = set()
        for i in nums:
            if i not in valid:
                valid.add(i)
            else:
                return True
        return False