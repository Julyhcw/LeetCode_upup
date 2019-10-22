class Solution:
    def divisorGame(self, N: int) -> bool:
        '''动态规划'''
        # f = [0 for i in range(N+1)]
        # f[1]=0
        # if N<=1: return 0
        # f[2]=1
        # for i in range(3,N+1):
        #     for j in range(1, i//2):
        #         if i % j == 0 and f[i-j]==0:
        #             f[i] = 1
        #             break
        # return f[N] == 1        
        
        '''数学归纳'''
        return False if N % 2 != 0 else True