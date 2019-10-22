class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:return False
        def sea_recu(l, r, u, d):
            if l > r or u > d:
                return False
            elif matrix[u][l] > target or matrix[d][r] < target:
                return False
            mid = l + (r-l) // 2
            row = u
            while row <= d and matrix[row][mid] <= target:
                if matrix[row][mid] == target:
                    return True
                row += 1
            return sea_recu(l, mid-1, row, d) or sea_recu(mid+1, r, u, row-1)
        return sea_recu(0, len(matrix[0])-1, 0, len(matrix)-1)
        
        
        '''T = O(m+n)'''
        # if not matrix:return False
        # m, n = len(matrix), len(matrix[0])
        # l, r = m-1, 0
        # while 0 <= l < m and r < n:
        #     if matrix[l][r] == target:
        #         return True
        #     elif matrix[l][r] > target:
        #         l -= 1
        #     else:
        #         r += 1
        # return False
                
            