from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = 0
        right = n - 1
        result = [0] * n
        postition = n - 1

        while left <= right:
            left_sqr = nums[left] ** 2
            right_sqr = nums[right] ** 2
            if left_sqr > right_sqr:
                result[postition] = left_sqr
                left += 1
            else:
                result[postition] = right_sqr
                right -= 1

            postition -= 1
        return result


sol = Solution()
print(sol.sortedSquares([-4, -1, 0, 3, 10]))
