class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        length = len(sorted(strs, key=lambda x:len(x))[0])
        s_len = len(strs)
        answer = ""
        for i in range(length):
            if self.check(i, strs, s_len):
                answer += strs[0][i]
            else:
                break
        return answer
        
    def check(self, idx, strs, s_len):
        for j in range(s_len):
            if strs[j][idx] != strs[j-1][idx]:
                return False
        return True