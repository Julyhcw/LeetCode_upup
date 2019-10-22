class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:return False
        i, j = max(nums)+1, max(nums)+1
        for a in range(len(nums)):
            if nums[a] <= i:
                i = nums[a]
            elif nums[a] <= j:
                j = nums[a]
            else:
                return True
        return False
            
