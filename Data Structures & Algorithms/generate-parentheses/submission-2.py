class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        curr = []
        def dfs(leftB,rightB):
            if leftB==rightB==n:
                res.append("".join(curr))
                return
            if leftB < n:
                curr.append('(')
                dfs(leftB+1,rightB)
                curr.pop()
            if rightB < leftB:
                curr.append(')')
                dfs(leftB,rightB+1)
                curr.pop()
        dfs(0,0)
        return res