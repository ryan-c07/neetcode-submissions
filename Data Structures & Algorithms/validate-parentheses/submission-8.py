class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for i in range(len(s)):
            if s[i] in '([{':
                stack.append(s[i])
            if (stack):
                if s[i] == ')':
                    if stack.pop() == '(':
                        continue
                    else:
                        return False
                if s[i] == '}':
                    if stack.pop() == '{':
                        continue
                    else:
                        return False
                if s[i] == ']':
                    if stack.pop() == '[':
                        continue
                    else:
                        return False
            else:
                return False
        return len(stack) == 0

