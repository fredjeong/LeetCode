class Solution:
    def __init__(self):
        self.answer = []
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != m * n:
            return self.answer
        
        temp = []
        for i in range(len(original)):
            temp.append(original[i])
            if i % n == n - 1:
                self.answer.append(temp)
                temp = []

        return self.answer
        