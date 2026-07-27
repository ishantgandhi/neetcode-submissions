class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        curr =[]
        def dfs(left,right):
            if left == right == n:
                res.append("".join(curr))
                return
            if left < n:
                curr.append('(')
                dfs(left+1,right)
                curr.pop()
            if right < left:
                curr.append(')')
                dfs(left,right+1)
                curr.pop()
        dfs(0,0)
        return res