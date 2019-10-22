class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if not nums:return '0'
        nums = list(map(str,nums))
        for i in range(len(nums)-1):
            swap = False
            for j in range(len(nums)-i-1):
                if int(nums[j]+nums[j+1]) < int(nums[j+1]+nums[j]):
                    nums[j], nums[j+1] = nums[j+1], nums[j]
                    swap = True
            if not swap:
                break
        ans = ''.join(nums)
        for i in ans:
            if i != '0':
                return ans  
        return str(int(ans))
                