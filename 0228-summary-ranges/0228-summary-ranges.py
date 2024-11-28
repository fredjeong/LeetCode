class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        length = len(nums)
        if length == 0:
            return []
        if length == 1:
            return [str(nums[0])]

        a = 0
        b = 0
        answer = []

        for i in range(length - 1):
            if nums[b] + 1 == nums[b + 1]:
                b += 1

            else:
                if a == b:
                    answer.append(str(nums[a]))

                else:
                    answer.append(str(nums[a]) + '->' + str(nums[b]))

                b += 1
                a = b
        if a == b:
            answer.append(str(nums[a]))

        else:
            answer.append(str(nums[a]) + '->' + str(nums[b]))

        return answer