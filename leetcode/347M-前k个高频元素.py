class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        fina = {}
        for i in nums:
            if i not in fina:
                fina[i] = 1
            else:
                fina[i] += 1
        fina = sorted(fina.items(), key=lambda x:x[1], reverse=True)
        ans = []
        for i in range(k):
            ans.append(fina[i][0])
        return ans