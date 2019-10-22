class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0:return True
        stack = [s[0]]
        bracket = {'(': 1, ')': -1, '[': 2, ']': -2, '{': 3, '}': -3}
        for i in s[1:]:
            if stack:
                if bracket[i] + bracket[stack[-1]] == 0:
                    stack.pop()
                else:
                    stack.append(i)
            else:
                stack.append(i)
        return len(stack) == 0