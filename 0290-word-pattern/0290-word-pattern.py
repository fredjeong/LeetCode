class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = list(s.split())
        pattern = list(pattern)
        if len(s) != len(pattern):
            return False
        if len(set(s)) != len(set(pattern)):
            return False

        dic = {}
        for i in range(len(s)):
            if s[i] not in dic:
                dic[s[i]] = pattern[i]
            else:
                if dic[s[i]] != pattern[i]:
                    return False
        return True