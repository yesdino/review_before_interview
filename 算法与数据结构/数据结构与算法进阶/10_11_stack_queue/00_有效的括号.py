class Solution:
    def isValid(self, str1: str) -> bool:
        stack = []
        mapping = {
            "]": "[",
            "}": "{",
            ")": "(",
        }
        for s in str1:
            if s in mapping:
                left = stack.pop() if stack else "#"
                if mapping[s] != left:
                    return False
            else:
                stack.append(s)
        return False if len(stack) else True

