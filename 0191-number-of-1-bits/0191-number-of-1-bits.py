class Solution:
    def hammingWeight(self, n: int) -> int:
        bin_n = bin(n)
        return bin_n.count("1")

        