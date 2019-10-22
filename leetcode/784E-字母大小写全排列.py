class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        n = len(S)
        fina = []
        if n == 0:return ['']
            
        def dfs(l,res):
            if l >= n or len(res) == n:   
                fina.append(res)
                return
            if S[l].isdigit():
                dfs(l+1,res+S[l])
            
            elif S[l].islower():
                dfs(l+1, res+S[l])
                dfs(l+1, res+S[l].upper())
            elif S[l].isupper():
                dfs(l+1, res+S[l])
                dfs(l+1, res+S[l].lower())

        dfs(0, '')
        return fina
              