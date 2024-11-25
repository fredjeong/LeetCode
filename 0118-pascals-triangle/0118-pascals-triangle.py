class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        dp = []
        dp.append([1])

        for i in range(1, numRows):
            temp = [0 for _ in range(i+1)]
            temp[0] = dp[i-1][0]
            temp[-1] = dp[i-1][-1]
            for j in range(1, i):
                temp[j] = dp[i-1][j-1] + dp[i-1][j]

            dp.append(temp)
        
        return dp