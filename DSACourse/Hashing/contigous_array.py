from collections import Counter
from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        hash_map = {0: -1}
        max_length = 0
        cum_sum = 0

        for i, num in enumerate(nums):

            cum_sum += 1 if num == 1 else -1

            if cum_sum in hash_map:

                max_length = max(max_length, i - hash_map[cum_sum])
            else:

                hash_map[cum_sum] = i

        return max_length


sol = Solution()
print(sol.findMaxLength([0, 1, 0, 1]))
