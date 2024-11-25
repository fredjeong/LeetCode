class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Return -1 if needle is not part of haystick
        if needle not in haystack:
            return -1
        
        return haystack.index(needle)