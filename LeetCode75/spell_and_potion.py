from typing import List


class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()

        result = []

        for spell in spells:

            required_strength = (success + spell - 1) // spell

            left, right = 0, len(potions)

            while left < right:
                mid = left + (right - left) // 2

                if potions[mid] >= required_strength:
                    right = mid
                else:
                    left = mid + 1

            successful_count = len(potions) - left

            result.append(successful_count)

        return result


solution = Solution()
print(solution.successfulPairs(
    spells=[5, 1, 3], potions=[1, 2, 3, 4, 5], success=7))
