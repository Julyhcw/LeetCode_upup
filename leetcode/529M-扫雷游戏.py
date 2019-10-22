class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        if not board:return board
        x, y = click[0], click[1]
        if board[x][y] == 'M':
            board[x][y] = 'X'
            return board
        m, n = len(board), len(board[0])
        visit = [[False for _ in range(n+1)] for _ in range(m+1)]
        direct = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
        def dfs(i,j):
            if board[i][j] == 'M' or visit[i][j] == True:
                return
            visit[i][j] = True
            count = 0
            for dir in direct:
                i_ = i + dir[0]
                j_ = j + dir[1]
                
                if 0 <= i_ < m and 0 <= j_ < n and board[i_][j_] == 'M':
                    count += 1
            if count > 0:
                board[i][j] = str(count)
            else:
                board[i][j] = 'B'
                
                for dir in direct:
                    i_ = i + dir[0]
                    j_ = j + dir[1]
                                    
                    if 0 <= i_ < m and 0 <= j_ < n and visit[i_][j_] == False:
                        dfs(i_,j_)
        dfs(x,y)
        return board