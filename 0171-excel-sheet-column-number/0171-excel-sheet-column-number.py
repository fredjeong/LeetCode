class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        dic = {}
        
        for i in range(26):
            dic[alphabet[i]] = i+1
        
        answer = 0
        length = len(columnTitle)
        for i in range(length):
            answer += dic[columnTitle[i]] * (26**(length - 1 - i))
        
        return answer
