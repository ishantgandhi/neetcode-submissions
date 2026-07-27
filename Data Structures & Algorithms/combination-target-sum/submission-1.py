class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i,curr,sub):
            if curr == target:
                res.append(sub.copy())
                return
            if i >= len(nums) or curr > target:
                return
            sub.append(nums[i])
            dfs(i,curr+nums[i],sub)
            sub.pop()
            dfs(i+1,curr,sub)
        dfs(0,0,[])
        return res