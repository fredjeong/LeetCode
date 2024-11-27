class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length = len(nums)
        if length == 1:
            k = 1
            return k
        
        idx = 0
        k = length
        while idx < length - 1:
            if nums[idx] == '_':
                break
            if nums[idx] == nums[idx+1]:
                del nums[idx]
                nums.append('_')
                k -= 1
            else:
                idx += 1
        
        return k