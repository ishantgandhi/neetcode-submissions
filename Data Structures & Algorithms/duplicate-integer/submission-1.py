class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        setnum = set()
        for num in nums:
            if num in setnum:
                return True
            setnum.add(num)
        return False