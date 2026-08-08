class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def xorcalc(lis):
            val = 0
            for num in lis:
                val ^= num
            return val
        res = 0
        def dfs(i,sub):
            nonlocal res
            if i == len(nums):
                res+= xorcalc(sub)
                return
            sub.append(nums[i])
            dfs(i+1,sub)
            sub.pop()
            dfs(i+1,sub)
        dfs(0,[])
        return res
