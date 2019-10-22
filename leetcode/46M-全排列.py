class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if n == 0:return []
        fina = []
        def back_trace(tmp,res):
            if not tmp:
                fina.append(res)
            for i in range(len(tmp)):
                back_trace(tmp[:i]+tmp[i+1:],res+[tmp[i]])
        back_trace(nums,[])
        return fina