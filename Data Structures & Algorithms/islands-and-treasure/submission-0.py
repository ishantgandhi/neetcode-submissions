class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        R,C = len(grid), len(grid[0])
        visit = set()
        q = deque()

        def bfs(r,c):
            if (min(r,c) < 0 or r >= R or c >= C or grid[r][c]== -1 or ((r,c)) in visit):
                return
            visit.add((r,c))
            q.append([r,c])


        for r in range(R):
            for c in range(C):
                if grid[r][c] == 0:
                    visit.add((r,c))
                    q.append([r,c])
        
        dist = 0
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                grid[r][c]= dist
                bfs(r+1,c)    
                bfs(r,c+1)    
                bfs(r-1,c)    
                bfs(r,c-1)  
            dist+=1  