class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        nlist = []
        for num in range(n+1):
            if num==0:
                continue
            nlist.append(num)
        print(nlist)
        def dfs(sub):
            if len(sub) == k and sub not in res:
                res.append(sub.copy())
                return 
            for num in nlist:
                if num in sub:
                    return
                sub.append(num)
                dfs(sub)
                sub.pop()
        dfs([])
        return res
        