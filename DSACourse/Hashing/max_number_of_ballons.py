from collections import Counter


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        char_count = Counter(text)
        required_counts = {
            "b": 1,
            "a": 1,
            "l": 2,
            "o": 2,
            "n": 1
        }

        max_instances = float("inf")

        for char, required in required_counts.items():
            max_instances = min(max_instances, char_count[char] // required)

        return max_instances


sol = Solution()
print(sol.maxNumberOfBalloons("loonbalxballpoon"))
