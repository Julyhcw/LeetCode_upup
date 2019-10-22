class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0]) 
        dires = [(-1,-1),(0,-1),(1,-1),(-1,0),(1,0),(-1,1),(0,1),(1,1)]
        fina = []         
        def dfs(i,j,cell_0,cell_1):
            for dir in dires:
                if i+dir[0] in range(0,m) and j+dir[1] in range(0,n):
                    if board[i+dir[0]][j+dir[1]] == 0:
                        cell_0 += 1
                    else:
                        cell_1 += 1
            return cell_0, cell_1
        for i in range(m):
            for j in range(n):
                cell_0 = 0
                cell_1 = 0
                cell_0, cell_1 = dfs(i,j,cell_0,cell_1)
                if board[i][j] == 0 and cell_1 == 3:fina.append([i,j,1])
                else:
                    if cell_1 < 2:fina.append([i,j,0])
                    if cell_1 > 3:fina.append([i,j,0])
        for f in fina:
            board[f[0]][f[1]] = f[2]
        return board
                    