class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:return 0
        n = len(nums)
        res_min, res_max = nums[0], nums[0]
        ans = nums[0]
        for i in range(1,n):
            tmp = [res_min*nums[i], res_max*nums[i], nums[i]]
            res_max, res_min = max(tmp), min(tmp)
            ans = max(ans, res_max)
        return ans