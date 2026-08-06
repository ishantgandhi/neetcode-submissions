class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i,cur,sub):
            if cur==target and sub not in res:
                res.append(sub.copy())
                return
            if cur > target or i >= len(nums):
                return
            sub.append(nums[i])
            dfs(i,cur+nums[i],sub)
            sub.pop()
            dfs(i+1,cur,sub)
        dfs(0,0,[])
        return res

