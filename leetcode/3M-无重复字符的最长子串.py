class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        queue = []
        fina = 0
        for i in s:
            if i not in queue:
                queue.append(i)
                #fina = max(fina,len(queue))
            else:
                fina = max(fina,len(queue))
                index = queue.index(i)
                queue = queue[index+1:]
                queue.append(i)
        return max(fina,len(queue)) if queue else 0