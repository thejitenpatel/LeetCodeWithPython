from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[j]:
                j += 1
                nums[j] = nums[i]

        return j + 1


sol = Solution()
print(sol.removeDuplicates([1, 1, 2]))
