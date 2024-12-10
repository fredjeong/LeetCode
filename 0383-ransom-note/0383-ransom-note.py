from collections import defaultdict

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dic_r = defaultdict(int)
        dic_m = defaultdict(int)

        for char in ransomNote:
            dic_r[char] += 1
        for char in magazine:
            dic_m[char] += 1

        for char in dic_r.keys():
            if dic_m[char] < dic_r[char]:
                return False
        return True