class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        fina = []
        n = len(candidates)
        candidates.sort()
        if n == 0:return []
        def bfs(l, tmp, res):
            if tmp == 0:
                fina.append(res)
                return
            for i in range(l, n):
                if tmp - candidates[i] < 0:
                    break
                bfs(i,tmp-candidates[i],res+[candidates[i]])

        bfs(0,target,[])
        return fina
