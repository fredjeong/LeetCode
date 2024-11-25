class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        if len(set(s)) != len(set(t)):
            return False

        dic = {}
        for i in range(len(s)):
            if s[i] in dic:
                if dic[s[i]] != t[i]:
                    return False
                else:
                    continue
            else:
                dic[s[i]] = t[i]

        return True