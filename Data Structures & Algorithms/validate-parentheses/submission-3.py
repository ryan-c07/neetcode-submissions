class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dictionary = { ")" : "(", "}" : "{", "]" : "[" }
        for p in s:
            if p in dictionary:
                if stack and stack[-1] == dictionary[p]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(p)
        return True if not stack else False