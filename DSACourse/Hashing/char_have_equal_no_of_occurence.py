from collections import defaultdict


class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        counts = defaultdict(int)

        for char in s:
            counts[char] += 1

        frequencies = counts.values()
        return len(set(frequencies)) == 1


sol = Solution()
print(sol.areOccurrencesEqual("abacbc"))
