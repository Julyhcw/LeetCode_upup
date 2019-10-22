class Solution:
    def romanToInt(self, s: str) -> int:
        roman_nums = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        i = 0
        fina = 0
        while i < len(s):
            if i+1 < len(s):
                if roman_nums[s[i]] < roman_nums[s[i+1]]:
                    fina += roman_nums[s[i+1]] - roman_nums[s[i]]
                    i += 2
                else:
                    fina += roman_nums[s[i]]
                    i += 1
            else:
                fina += roman_nums[s[i]]
                i += 1
        return fina
        
        
        # roman_nums = {'I':1,'IV':4,'V':5,'IX':9,'X':10,
        #       'XL':40,'L':50,'XC':90,'C':100,
        #        'CD':400,'D':500,'CM':900,'M':1000}
        # i = 0
        # fina = 0
        # while i < len(s):
        #     if i+1 < len(s):
        #         if s[i:i+2] in roman_nums:
        #             fina += roman_nums[s[i:i+2]]
        #             i += 2
        #         else:
        #             fina += roman_nums[s[i]]
        #             i += 1
        #     else:
        #         fina += roman_nums[s[i]]
        #         i += 1
        # return fina