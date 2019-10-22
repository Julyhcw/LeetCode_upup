class Solution:
    def reverseVowels(self, s: str) -> str:
        i, j = 0, len(s) - 1
        chars = ['a', 'o', 'u', 'e', 'i','A','O','E','I','U']
        s = list(s)
        while i < j:
            if s[i] in chars and i < j:
                if s[j] in chars and i <j:
                    s[i], s[j] = s[j], s[i]
                    i += 1
                    j -= 1
                else:
                    j -= 1
            else:
                if i >= j:
                    break
                else:
                    i += 1
        return ''.join(s)