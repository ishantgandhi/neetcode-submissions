class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []

        def dfs(lB,rB):
            if lB == rB == n:
                res.append("".join(stack))
                return
            if lB < n:
                stack.append('(')
                dfs(lB+1,rB)
                stack.pop()
            if rB < lB:
                stack.append(')')
                dfs(lB,rB+1)
                stack.pop()
        dfs(0,0)
        return res
