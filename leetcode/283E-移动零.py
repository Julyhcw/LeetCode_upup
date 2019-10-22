class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        '''遍历数组，遇到不是0的就放置到前面'''
        i, j = 0, 0
        for j in range(len(nums)):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j],nums[i]
                i += 1
                
#         for i in nums:
#             if i == 0:
#                 nums.append(0)
#                 nums.remove(0)
        
