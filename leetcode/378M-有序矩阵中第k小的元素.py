class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        def count_num(m, target):
            i, j = 0, len(m)-1
            ans = 0
            while i < len(m) and j >= 0:
                if m[i][j] <= target:
                    ans += j+1
                    i += 1
                else:
                    j -= 1
            return ans
        l, r = matrix[0][0], matrix[-1][-1]
        while l < r:
            mid = (l+r) // 2
            count = count_num(matrix, mid)
            if count < k:
                l = mid + 1
            else:
                r = mid
        return l