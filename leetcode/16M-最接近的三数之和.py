class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        ##排序+双指针
        n = len(nums)
        nums.sort()
        fina = 9999999
        ans = 0
        for i in range(n-2):
            l, r = i+1, n-1
            while l < r:
                tmp = nums[i] + nums[l] + nums[r]
                res = abs(tmp-target)
                if res == 0:return target
                if tmp < target:
                    l += 1
                elif tmp > target:
                    r -= 1
                if res < fina:
                    fina = res
                    ans = tmp
        return ans
           
        ##暴力  竟然过了。。。
        # n = len(nums)
        # fina = 9999999
        # ans = 0
        # for i in range(n-2):
        #     for j in range(i+1, n-1):
        #         for k in range(j+1, n):
        #             tmp = nums[i]+nums[j]+nums[k]
        #             res = abs(tmp-target)
        #             if res == 0:return tmp
        #             if res < fina:
        #                 fina = res
        #                 ans = tmp
        # return ans