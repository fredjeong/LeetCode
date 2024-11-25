from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        # Open brackets must be closed by the same type of brackets
        # Open brackets must be closed in the correct order
        # Every close bracket has a corresponding open bracket of the same type

        stack = deque()
        if s[0] in [")", "}", "]"]:
            return False
        stack.append(s[0])

        dic = {")": "(", "}": "{", "]": "["}
        
        for i in range(1, len(s)):
            if s[i] in [")", "}", "]"]:
                if stack:
                    temp = stack.pop()
                    if temp != dic[s[i]]:
                        return False
                else:
                    return False
            elif s[i] in ["(", "{", "["]:
                stack.append(s[i])
        
        if stack:
            return False
        
        return True