class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        '''双端队列'''
        if k <= 1:return nums
        n = len(nums)
        ans = [0]*(n-k+1)
        i, j = 0, n
        while i <= j-k:
            ans[i] = max(nums[i:i+k])
            ans[j-k] = max(nums[j-k:j])
            i += 1
            j -= 1
        return ans
                
        # if k <= 1:return nums
        # ans = []
        # for i in range(len(nums)-k+1):
        #     ans.append(max(nums[i:i+k]))
        # return ans