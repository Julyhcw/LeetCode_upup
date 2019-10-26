class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res = []
        for i in range(n-3):
            tar = target - nums[i]
            for j in range(i+1, n-2):
                l, r = j+1, n-1
                while l < r:
                    tmp = nums[j] + nums[l] + nums[r]
                    if tmp == tar:
                        ans = [nums[i], nums[j], nums[l], nums[r]]
                        if ans not in res:
                            res.append(ans)
                        l += 1
                        r -= 1
                    elif tmp < tar:
                        l += 1
                    else:
                        r -= 1
        return res