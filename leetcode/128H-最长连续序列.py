class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:return n
        nums.sort()
        ans = 1
        tmp = 1
        for i in range(n-1):
            if nums[i] + 1 == nums[i+1]:
                tmp += 1
            elif nums[i] == nums[i+1]:
                continue
            else:
                ans = max(ans, tmp)
                tmp = 1
        ans = max(ans,tmp)
        return ans
        
        