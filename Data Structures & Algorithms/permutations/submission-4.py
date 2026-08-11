class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(sub):
            if len(sub) == len(nums) and sub not in res:
                res.append(sub.copy())
                return
            for num in nums:
                if num in sub:
                    continue
                sub.append(num)
                dfs(sub)
                sub.pop()
        dfs([])
        return res