class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = nums.count(val)
        for _ in range(count):
            nums.remove(val)
            nums.append('_')

        k = len(nums) - count

        return k