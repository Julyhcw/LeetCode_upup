class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        ans_map = {}
        for a in A:
            for b in B:
                if a+b not in ans_map:
                    ans_map[a+b] = 1
                else:
                    ans_map[a+b] += 1
        ans = 0
        for c in C:
            for d in D:
                if -(c+d) in ans_map:
                    ans += ans_map[-(c+d)]
        return ans