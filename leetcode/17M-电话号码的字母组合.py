class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:return []
        nums_char = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        fina = ['']
        for a in digits:
            fina = [i+j for i in fina for j in nums_char[a]]
        return fina