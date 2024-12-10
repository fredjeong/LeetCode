from collections import deque

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s = deque(s)
        t = deque(t)

        while s:
            check = False
            char_s = s.popleft()
            while t:
                char_t = t.popleft()
                if char_t == char_s:
                    check = True
                    break
            
            if not check:
                return False
        
        return True