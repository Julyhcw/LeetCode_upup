class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        # mag = list(magazine)
        # for i in ransomNote:
        #     if i in mag:
        #         mag.remove(i)
        #     else:
        #         return False
        # return True
        '''哈希'''
        mag = {}
        for i in magazine:
            if i not in mag:
                mag[i] = 1
            else:
                mag[i] += 1
        for j in ransomNote:
            if j in mag:
                if mag[j] == 0:
                    return False
                else:
                    mag[j] -= 1
            else:
                return False
        return True