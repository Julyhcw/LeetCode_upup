class Solution:
    def intToRoman(self, num: int) -> str:
        roman = ['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
        nums = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        i = 0
        fina = ''
        while i < 13:
            while num >= nums[i]:
                fina += roman[i]
                num -= nums[i]
            i += 1
            if num == 0:
                break
        return fina
            
            
            