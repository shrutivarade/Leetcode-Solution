class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        # DFS
        row, col = len(grid), len(grid[0])
        islands = 0
        def dfs(r,c,grid):         
            grid[r][c] = "0"    # mark the visited 1's and 0's
            if r < row -1 and grid[r+1][c] == "1":
                dfs(r+1,c,grid)
            if r > 0 and grid[r-1][c] == "1":
                dfs(r-1,c,grid)
            if c < col -1 and grid[r][c+1] == "1":
                dfs(r,c+1,grid)
            if c > 0 and grid[r][c-1] == "1":
                dfs(r,c-1,grid)

        for r in range(row):
            for c in range(col):
                if grid[r][c] == "1":
                    dfs(r,c,grid)
                    islands+=1
        return islands
        


        # BFS
        rows, cols = len(grid), len(grid[0])
        islands = 0
        visited = set()

        def bfs(r,c): # this function is responsible to all the connect 1's in visited set
            q = collections.deque()
            visited.add((r,c))
            q.append((r,c))
            while q:
                row, col = q.popleft()
                directions = [[1,0], [-1,0], [0,1], [0,-1]] # all four directions
                
                for dr, dc in directions:
                    r = row+dr
                    c = col+dc
                    if (r in range(rows) and c in range(cols) and grid[r][c] == "1" and (r,c) not in visited):
                        q.append((r,c))
                        visited.add((r,c))


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    bfs(r,c)
                    islands+=1
        
        return islands