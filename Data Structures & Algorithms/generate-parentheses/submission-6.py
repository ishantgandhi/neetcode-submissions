class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(ob,cb,sub):
            if ob == cb == n and sub not in res:
                res.append(''.join(sub.copy()))
                return
            if ob < n:
                sub.append('(')
                dfs(ob+1,cb,sub)
                sub.pop()
            if cb < ob:
                sub.append(')')
                dfs(ob,cb+1,sub)
                sub.pop()
        dfs(0,0,[])
        return res
                
            