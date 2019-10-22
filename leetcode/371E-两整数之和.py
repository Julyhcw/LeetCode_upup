class Solution:
    def getSum(self, a: int, b: int) -> int:
        fina_0 = a ^ b
        fina_1 = a & b
        fina = (fina_1 << 1) + fina_0
        return fina