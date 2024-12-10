from collections import defaultdict

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        dic_s = defaultdict(int)
        dic_t = defaultdict(int)

        for char in s:
            dic_s[char] += 1
        for char in t:
            dic_t[char] += 1
        
        for char in dic_t.keys():
            if dic_s[char] != dic_t[char]:
                return char