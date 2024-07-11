from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        prefix = [nums[0]]

        for i in range(1, len(nums)):
            prefix.append(nums[i] + prefix[-1])

        return prefix


sol = Solution()
print(sol.runningSum([1, 2, 3, 4]))
