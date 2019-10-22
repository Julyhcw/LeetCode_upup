class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        '''递归回溯'''
        fina = []
        def back_recu(l,res):
            fina.append(res)
            for j in range(l,len(nums)):
                back_recu(j+1,res+[nums[j]])
        back_recu(0,[])
        return fina
            