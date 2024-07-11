from typing import List


class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        cumlative_sum = 0
        min_cumlative_sum = 0

        for num in nums:
            cumlative_sum += num
            min_cumlative_sum = min(min_cumlative_sum, cumlative_sum)

        return 1 - min_cumlative_sum


sol = Solution()
print(sol.minStartValue(nums=[-3, 2, -3, 4, 2]))
