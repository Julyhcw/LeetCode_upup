class Solution:
    def myAtoi(self, s: str) -> int:
        fina = 0
        s = s.lstrip()
        if len(s) == 0:return 0
        i = 2 if s[0] == '-' or s[0] == '+' else 1
        while i <= len(s):
            try:
                fina = int(s[:i])
                i += 1
            except:
                break
        if fina > 2 ** 31 - 1: return 2 ** 31 - 1
        if fina < -2 ** 31:
            return - 2 ** 31
        else:
            return fina
            