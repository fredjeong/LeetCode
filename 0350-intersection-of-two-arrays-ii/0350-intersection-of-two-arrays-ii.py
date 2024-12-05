from collections import defaultdict

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic_1 = defaultdict(int)
        dic_2 = defaultdict(int)

        for num in nums1:
            dic_1[num] += 1
        for num in nums2:
            dic_2[num] += 1
        
        answer = []
        for key in list(set(dic_1.keys()) & set(dic_1.keys())):
            for _ in range(min(dic_1[key], dic_2[key])):
                answer.append(key)
        
        return answer
