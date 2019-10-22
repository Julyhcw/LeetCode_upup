class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:return 0 #is None: return 0
        n = len(needle)
        i = 0
        #for i in haystack:
        while i < len(haystack):
            if haystack[i] == needle[0]:
                if haystack[i:i+n] == needle:
                    return i
                else:
                    i += 1
            else:
                i += 1
        return -1