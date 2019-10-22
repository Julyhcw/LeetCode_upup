class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        import collections
        ticks = collections.defaultdict(list)
        for f,t in tickets:
            ticks[f].append(t)
        fina = []
        def dfs(s):
            if len(ticks[s]) > 1:
                ticks[s].sort()
            while ticks[s]:
                dfs(ticks[s].pop(0))
            fina.append(s)
        dfs('JFK')
        return fina[::-1]
        
