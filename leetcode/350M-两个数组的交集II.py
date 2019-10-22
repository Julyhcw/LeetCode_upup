class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        i, j = 0, 0
        fina = []
        #n = min(len(nums1), len(nums2))
        while i < len(nums1) and j < len(nums2):
        #for index in range(min(len(nums1), len(nums2))):
            if nums1[i] == nums2[j]:
                fina.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return fina
        
        
        # if not nums1 or not nums2:return
        # def mixset(s1,s2):
        #     fina = []
        #     for i in s1:
        #         if i in s2:
        #             fina.append(i)
        #             s2.remove(i)
        #     return fina
        # m, n = len(nums1), len(nums2)
        # if m < n:
        #     res = mixset(nums1, nums2)
        # else:
        #     res = mixset(nums2, nums1)
        # return res