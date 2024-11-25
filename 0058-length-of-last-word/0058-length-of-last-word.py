class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = list(s.strip().split())
        return len(s[-1])