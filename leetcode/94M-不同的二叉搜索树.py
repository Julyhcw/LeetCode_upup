class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0]*(n+1)
        dp[0],dp[1] = 1, 1
        for i in range(2,n+1):
            for j in range(1, i+1):
                dp[i] += dp[j-1]*dp[i-j]
        return dp[-1]
##每个节点轮流作为根节点，总的可能性为左子树的可能性*右子树总的可能性