class Solution:
    def countAndSay(self, n: int) -> str:
        #if n == 0 or 1:return '1'
        fina = '1'
        for i in range(1,n):
            tmp = ''
            n = 1
            res = fina[0]
            for j in range(1,len(fina)):
                if fina[j] == res:
                    n += 1
                else:
                    tmp += str(n) + res
                    n = 1
                    res = fina[j]
            tmp += str(n)+res
            fina = tmp
        return fina