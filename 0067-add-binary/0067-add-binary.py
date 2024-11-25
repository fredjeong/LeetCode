class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = "0b" + a
        b = "0b" + b
        
        # sum in integer form
        s = int(a, 2) + int(b, 2)

        # convert the integer to binary string
        s = bin(s)

        # remove the "0b" part
        return s[2:]

