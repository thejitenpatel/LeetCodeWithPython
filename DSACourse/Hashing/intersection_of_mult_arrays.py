from collections import defaultdict
from typing import List


class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        counts = defaultdict(int)

        for num in nums:
            for x in num:
                counts[x] += 1

        ans = []
        for key in counts:
            if counts[key] == len(nums):
                ans.append(key)

        return sorted(ans)
sol = Solution()
print(sol.intersection([[3, 1, 2, 4, 5], [1, 2, 3, 4], [3, 4, 5, 6]]))
