from typing import List


class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        averages = [-1] * n

        if k == 0:
            return nums
        
        window_size = 2 * k + 1

        if window_size > n:
            return averages
        
        window_sum = sum(nums[:window_size])
        averages[k] = window_sum // window_size

        for i in range(window_size, n):
            window_sum = window_sum - nums[i - window_size] + nums[i]
            averages[i - k] = window_sum // window_size
        return averages



sol = Solution()
print(sol.getAverages([7, 4, 3, 9, 1, 8, 5, 2, 6], k=3))
