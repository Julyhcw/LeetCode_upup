class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if not nums:return
        fina = set()
        for i in range(len(nums)):
            if nums[i] in fina:
                return True
            else:
                fina.add(nums[i])
        return False