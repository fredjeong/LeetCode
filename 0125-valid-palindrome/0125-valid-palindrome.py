import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub('[^A-Za-z0-9]', '', s)
        s = s.lower()

        length = len(s)

        for i in range(length//2):
            if s[i] != s[length-1-i]:
                return False

        return True