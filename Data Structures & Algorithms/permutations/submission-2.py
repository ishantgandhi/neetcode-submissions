class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(nums,sub):
            if len(sub) == len(nums):
                res.append(sub.copy())
                return

            
            for num in nums:
                if num in sub:
                    continue
                sub.append(num)
                dfs(nums,sub)
                sub.pop()
        dfs(nums,[])
        return res
