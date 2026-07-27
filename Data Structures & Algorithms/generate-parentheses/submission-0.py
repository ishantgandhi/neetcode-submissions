class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []

        def dfs(oN,cN):
            if oN == cN == n:
                res.append("".join(stack))
                return
            if oN < n:
                stack.append("(")
                dfs(oN+1,cN)
                stack.pop()
            if cN < oN:
                stack.append(")")
                dfs(oN,cN+1)
                stack.pop()
        dfs(0,0)
        return res