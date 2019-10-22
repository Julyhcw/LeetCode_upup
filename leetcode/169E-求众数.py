class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums) < 2:return nums[0]
        nums.sort()
        return nums[len(nums)//2]
        
        # tmp = len(nums) // 2
        # res, ans = 1, 0
        # fina = nums[0]
        # for i in range(1,len(nums)):
        #     # res = 1
        #     if nums[i] == nums[i-1]:
        #         res += 1
        #         if res > tmp:return nums[i]
        #     else:
        #         res = 1

        
        
