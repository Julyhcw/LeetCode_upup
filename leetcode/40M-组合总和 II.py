class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        if n == 0:return []
        candidates.sort()
        fina = []
        def back_trace(l,tmp,res):
            if tmp == 0:
                if res not in fina:
                    fina.append(res)
                return
            for i in range(l,n):
                if tmp - candidates[i] < 0:
                    break
                back_trace(i+1,tmp-candidates[i],res+[candidates[i]])
        back_trace(0,target,[])
        return fina