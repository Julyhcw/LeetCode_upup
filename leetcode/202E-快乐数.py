class Solution:
    def isHappy(self, n: int) -> bool:
        fina = set()
        #i = 0
        while n != 1:
            i = 0 
            while n > 0:
                tmp = n % 10
                i += tmp**2
                n //= 10
            if i in fina:
                return False
            else:
                fina.add(i)
            n = i
        return True