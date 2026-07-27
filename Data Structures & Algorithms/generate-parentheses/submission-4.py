class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        curr = []
        def dfs(lb,rb):
            if lb == rb == n:
                res.append("".join(curr))
                return
            if lb < n:
                curr.append('(')
                dfs(lb+1,rb)
                curr.pop()
            if rb < lb:
                curr.append(')')
                dfs(lb,rb+1)
                curr.pop()
        dfs(0,0)
        return res