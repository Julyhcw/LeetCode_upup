class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:return []
        fina = []
        def back_trace(tmp, res):
            if not tmp and res not in fina:
                fina.append(res)
            for i in range(len(tmp)):
                if i == 0:
                    back_trace(tmp[:i]+tmp[i+1:], res+[tmp[i]])
                if i-1 >=0:
                    if tmp[i] != tmp[i-1]:
                        back_trace(tmp[:i]+tmp[i+1:], res+[tmp[i]])
        back_trace(nums,[])
        return fina
            