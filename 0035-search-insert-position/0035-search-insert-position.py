class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        length = len(nums)

        if target > nums[-1]:
            return length
        elif target < nums[0]:
            return 0

        idx_1 = 0
        idx_2 = length - 1

        while idx_2 - idx_1 > 1:
            if target == nums[(idx_1 + idx_2) // 2]:
                return (idx_1 + idx_2) // 2

            if target < nums[(idx_1 + idx_2) // 2]:
                idx_2 = (idx_1 + idx_2) // 2
            else:
                idx_1 = (idx_1 + idx_2) // 2

        if target > nums[idx_1]:
            return idx_1 + 1
        else:
            return idx_1