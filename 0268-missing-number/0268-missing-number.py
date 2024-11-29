class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        maximum = max(nums)
        result = {i for i in range(maximum)} - set(nums)
        if result:
            return list(result)[0]
        else:
            return maximum + 1


        