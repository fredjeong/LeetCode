class Solution:
    def climbStairs(self, n: int) -> int:
        answer = 0
        for two in range(n//2+1):
            one = n - 2 * two
            answer += self.combination(two, one)
        
        return answer
    
    def combination(self, two, one):
        numerator = 1
        denominator = 1
        for i in range(two):
            denominator *= i + 1
            numerator *= two + one - i
        return numerator // denominator