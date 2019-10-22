class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if len(board) == 0 or len(board[0]) == 0:
            return
        def dfs(nums, x, y):
            if x < 0 or x >= row or y < 0 or y >= col or nums[x][y] != 'O':
                return
            nums[x][y] = '*'
            dfs(nums, x - 1, y)
            dfs(nums, x, y + 1)
            dfs(nums, x + 1, y)
            dfs(nums, x, y - 1)
        row, col = len(board), len(board[0])
        for i in range(row):
            dfs(board, i, 0)
            dfs(board, i, col - 1)
        for j in range(col):
            dfs(board, 0, j)
            dfs(board, row - 1, j)
        for i in range(row):
            for j in range(col):
                if board[i][j] == '*':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'