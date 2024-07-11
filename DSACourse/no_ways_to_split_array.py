from typing import List


class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        # n = len(nums)

        # prefix = [nums[0]]
        # for i in range(1, n):
        #     prefix.append(nums[i] + prefix[-1])

        # ans = 0
        # for i in range(n-1):
        #     left_section = prefix[i]
        #     right_section = prefix[-1] - prefix[i]
        #     if left_section >= right_section:
        #         ans += 1
        # return ans
        ans = left_section = 0
        total = sum(nums)

        for i in range(len(nums) - 1):
            left_section += nums[i]
            right_section = total - left_section

            if left_section >= right_section:
                ans += 1
        return ans


sol = Solution()
print(sol.waysToSplitArray(nums=[2, 3, 1, 0]))
