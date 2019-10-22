class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:      
        # if len(cost) < 3:
        #     return min(cost)
        p,q = 0, 0
        for i in range(2,len(cost)+1):
            p, q = q, min(q+cost[i-1], p+cost[i-2])
        return q