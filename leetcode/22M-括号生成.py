class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        '''回溯法递归'''
        fina = []
        def back(res = '',l=0,r=0):
            if len(res) == 2*n:
                fina.append(res)
                #return 
            if l < n:
                back(res + '(',l+1,r)
            if r < l:
                back(res+')',l,r+1)
        back()
        return fina
            
