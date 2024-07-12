from typing import List


class Solution:
    def countElements(self, arr: List[int]) -> int:
        num_set = set(arr)
        count = 0
        for num in arr:
            if num + 1 in num_set:
                count += 1
        return count

sol = Solution()
print(sol.countElements([1, 1, 3, 3, 5, 5, 7, 7]))
