class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        R,C = len(grid),len(grid[0])
        visit = set()
        def dfs(r,c):
            if (r >= R or c >= C or r < 0 or c < 0 or grid[r][c]==0 or (r,c) in visit):
                return 0
            visit.add((r,c))
            count = 1
            
            count+= dfs(r+1,c)
            count+= dfs(r,c+1)
            count+= dfs(r-1,c)
            count+= dfs(r,c-1)

            return count
        area = 0
        for r in range(R):
            for c in range(C):
                area = max(area,dfs(r,c))
        return area