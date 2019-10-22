class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ans = 0
        for i in tokens:
            if i in ['+', '-', '*', '/']:
                m, n = stack.pop(), stack.pop()
                tmp = str(int(eval(n + i + m)))
                stack.append(tmp)
            else:
                stack.append(i)
        return stack[-1]