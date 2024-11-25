class Solution:
    def mySqrt(self, x: int) -> int:
        num = 0
        while True:
            if (num+1) ** 2 > x:
                break
            else:
                num += 1
        return num

