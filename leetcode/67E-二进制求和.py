class Solution:
    def addBinary(self, a: str, b: str) -> str:
        n = 0
        fina = ''
        a_len, b_len = len(a), len(b)
        if a_len > b_len:
            b = '0'*(a_len-b_len)+b
        else:
            a = '0'*(b_len-a_len)+a
        for i in range(len(a)-1,-1,-1):
            x = int(a[i]) + int(b[i]) + n
            if x == 3:
                fina = '1' + fina
                n = 1
            elif x == 2:
                fina = '0' + fina
                n = 1
            elif x == 1:
                fina = '1' + fina
                n = 0
            else:
                fina = '0' + fina
                n = 0
        if n == 1:
            fina = '1'+fina
        return fina
