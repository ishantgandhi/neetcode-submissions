class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def dfs(i,cur,sub):
            if cur == target and sub not in res:
                res.append(sub.copy())
                return
            if i >= len(candidates) or cur > target:
                return
            sub.append(candidates[i])
            dfs(i+1,cur+candidates[i],sub)
            sub.pop()
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i+=1
            dfs(i+1,cur,sub)
        dfs(0,0,[])
        return res


