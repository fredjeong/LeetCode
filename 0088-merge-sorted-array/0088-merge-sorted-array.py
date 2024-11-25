class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = 0 # idx for nums1
        j = 0 # idx for nums2

        while j < n:
            print(nums1)
            if nums1[i] >= nums2[j] or i >= m + j:
                nums1.pop()
                nums1.insert(i, nums2[j])
                i += 1
                j += 1
            else:
                i += 1