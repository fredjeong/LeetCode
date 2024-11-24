from collections import defaultdict

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dic = defaultdict(int)

        for num in nums:
            dic[num] += 1
        for num in set(nums):
            if dic[num] == 1:
                return num