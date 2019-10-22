class Solution:
    def maxProfit(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:return 0
        dp1 = [0]*n
        dp2 = [0]*n
        min_profit, max_profit = nums[0], nums[-1]
        for i in range(1,n):
            dp1[i] = max(dp1[i-1], nums[i]-min_profit)
            min_profit = min(min_profit,nums[i])
        for j in range(n-2, -1, -1):
            dp2[j] = max(dp2[j+1], max_profit-nums[j])
            max_profit = max(max_profit, nums[j])
        ans = [dp1[_] + dp2[_] for _ in range(n)]
        return max(ans)