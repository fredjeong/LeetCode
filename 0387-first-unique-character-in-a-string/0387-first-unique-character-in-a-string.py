class Solution:
    def firstUniqChar(self, s: str) -> int:
        indices = []
        for char in set(s):
            if s.count(char) != 1:
                continue
            if s.count(char) == 1:
                indices.append(s.index(char))
        
        if indices:
            return min(indices)
        else:
            return -1