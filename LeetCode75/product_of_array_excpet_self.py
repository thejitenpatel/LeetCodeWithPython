from typing import List


class Solution:

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        n = len(nums)
        prefix = [1] * n
        suffix = [1] * n
        answer = [1] * n

        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i - 1]

        for i in range(n-2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]

        for i in range(n):
            answer[i] = prefix[i] * suffix[i]

        return answer
        """

        n = len(nums)
        answer = [1] * n

        prefix = 1
        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]

        return answer


sol = Solution()
print(sol.productExceptSelf(nums=[1, 2, 3, 4]))
