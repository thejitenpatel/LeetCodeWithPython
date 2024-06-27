from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occurences = {}

        for i in arr:
            if i in occurences:
                occurences[i] += 1
            else:
                occurences[i] = 1

        occurrence_counts = list(occurences.values())

        unique_counts = set(occurrence_counts)

        return len(occurrence_counts) == len(unique_counts)


sol = Solution()
print(sol.uniqueOccurrences(arr=[1, 2, 2, 1, 1, 3]))
