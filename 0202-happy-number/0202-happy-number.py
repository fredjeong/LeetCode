class Solution:
    def isHappy(self, n: int) -> bool:
        n = str(n)

        s = set()
        while n != str(1):
            if n in s:
                return False

            s.add(n)

            new_num = 0
            for i in range(len(n)):
                new_num += int(n[i])**2
            n = str(new_num)

        if n == str(1):
            return True
        
        return False