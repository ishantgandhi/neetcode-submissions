class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        R,C = len(grid),len(grid[0]) 
        visit = set()
        q = deque()
        fresh = 0
        time = 0
        
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1:
                    fresh +=1
                if grid[r][c] == 2:
                    q.append((r,c))
                    visit.add((r,c))

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while fresh > 0 and q:
            l = len(q)
            for i in range(l):
                r,c = q.popleft()
                for dr,dc in directions:
                    row,col = r+dr,c+dc
                    if (row in range(len(grid)) and
                        col in range(len(grid[0])) and 
                        grid[row][col] == 1 and (row,col) not in visit):
                        q.append((row,col))
                        visit.add((row,col))
                        fresh -=1
            time+=1
        return time if fresh == 0 else -1

