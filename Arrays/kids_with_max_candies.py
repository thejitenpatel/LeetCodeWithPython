from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        current_max_candies = max(candies)
        ans = []

        for i in candies:
            ans.append(i + extraCandies >= current_max_candies)
        return ans


sol = Solution()
print(sol.kidsWithCandies([2, 3, 5, 1, 3], 3))
