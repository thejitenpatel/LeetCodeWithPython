from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        current_sum = sum(nums[:k])
        max_sum = current_sum

        for i in range(k, len(nums)):
            current_sum += nums[i] - nums[i - k]
            if current_sum > max_sum:
                max_sum = current_sum

        return max_sum / k


sol = Solution()
print(sol.findMaxAverage(nums=[1, 12, -5, -6, 50, 3], k=4))
