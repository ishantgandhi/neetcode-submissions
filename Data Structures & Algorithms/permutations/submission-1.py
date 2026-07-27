class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(nums,sub):
            if len(sub)==len(nums):
                res.append(sub.copy())
            
            for num in nums:
                if num in sub:
                    continue
                
                sub.append(num)
                backtrack(nums,sub)
                sub.pop()
        backtrack(nums,[])
        return res