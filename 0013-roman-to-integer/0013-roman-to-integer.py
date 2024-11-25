class Solution:
    def romanToInt(self, s: str) -> int:
        num = 0
        length = len(s)
        
        i = 0
        while i < length:
            if s[i] == "I":
                if i < length-1 and s[i+1] == "V":
                    num += 4
                    i += 2
                elif i < length-1 and s[i+1] == "X":
                    num += 9
                    i += 2
                else:
                    num += 1
                    i += 1
            
            elif s[i] == "V":
                num += 5
                i += 1
            
            elif s[i] == "X":
                if i < length-1 and s[i+1] == "L":
                    num += 40
                    i += 2
                elif i < length-1 and s[i+1] == "C":
                    num += 90
                    i += 2
                else:
                    num += 10
                    i += 1

            elif s[i] == "L":
                num += 50
                i += 1
            
            elif s[i] == "C":
                if i < length-1 and s[i+1] == "D":
                    num += 400
                    i += 2
                elif i < length-1 and s[i+1] == "M":
                    num += 900
                    i += 2
                else:
                    num += 100
                    i += 1
            
            elif s[i] == "D":
                num += 500
                i += 1
            
            elif s[i] == "M":
                num += 1000
                i += 1

        return num