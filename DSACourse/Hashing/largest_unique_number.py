from collections import Counter
from typing import List


class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        cntr = Counter(nums)
        biggest = -1

        for num, freq in cntr.items():
            if freq == 1:
                biggest = max(biggest, num)
        return biggest
        # counts = defaultdict(int)

        # for num in nums:
        #     counts[num] += 1

        # result = -1

        # for num, cnt in counts.items():
        #     if cnt == 1 and num > result:
        #         result = num

        # return result


sol = Solution()
print(sol.largestUniqueNumber([5, 7, 3, 9, 4, 9, 8, 3, 1]))
