from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        pars = {')':'(', '}':'{', ']':'['}

        for c in s:
            if c in pars.values():
                stack.append(c)
            else:
                if len(stack) == 0 or pars[c] != stack.pop():
                    return False
                
        return True and len(stack) == 0