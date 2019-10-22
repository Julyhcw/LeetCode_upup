class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:return 0
        n,m = len(grid), len(grid[0])
        def dfs(i,j):
            if i not in range(n) or j not in range(m) or grid[i][j] != '1':
                return
            grid[i][j] = '0'
            dfs(i-1,j)
            dfs(i,j-1)
            dfs(i+1,j)
            dfs(i,j+1)
        fina = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    dfs(i,j)
                    fina += 1
        return fina
