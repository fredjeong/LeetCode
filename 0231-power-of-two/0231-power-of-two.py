class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 1:
            return False        

        x = 0
        while x < 32:
            if 2 ** x == n or 2 ** x == -1 * n:
                return True
            x += 1

        return False