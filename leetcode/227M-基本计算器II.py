class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(' ','',-1)
        stack = []
        i,j = 0,1
        tmp = 0
        while i < len(s):
            if s[i].isdigit():
                tmp = 10*tmp + int(s[i])
                if i+1 < len(s):
                    #if not s[i+1].isdigit():
                    if s[i+1] in ['+','-','*','/']:
                        stack.append(tmp)
                        tmp = 0
                elif i+1 == len(s):
                    stack.append(tmp)
                i += 1
            else:
                # stack.append(tmp)
                # tmp = 0
                if s[i] in ['+', '-']:
                    stack.append(s[i])
                    i += 1
                else:
                    res = s[i]
                    while i+1 < len(s):
                        if s[i+1].isdigit():
                            tmp = tmp*10 + int(s[i+1])
                            i += 1
                        else:
                            break
                    if res == '*':
                        tmp_new = stack.pop()*tmp
                    else:
                        tmp_new = int(stack.pop() / tmp)
                    stack.append(tmp_new)
                    i += 1
                    tmp = 0
        ans = stack[0]
        while j < len(stack):
            if stack[j] == '+':
                ans += stack[j + 1]
                j += 2
            elif stack[j] == '-':
                ans -= stack[j + 1]
                j += 2
            else:
                j += 1
        return ans
        

                        