from typing import List


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1 = set(nums1)
        set2 = set(nums2)

        answer = []

        distinct_nums1 = list(set1 - set2)

        distinct_nums2 = list(set2 - set1)

        answer.append(distinct_nums1)
        answer.append(distinct_nums2)

        return answer


solution = Solution()
print(solution.findDifference([1, 2, 3, 3], [1, 1, 2, 2]))
