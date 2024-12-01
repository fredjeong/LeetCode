class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n < 1:
            return False
        for i in range(21):
            if n == 3**i:
                return True
        return False