class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums) < 1:return nums[0]
        ans = nums[0]
        for i in nums[1:]:
            ans ^= i
        return ans