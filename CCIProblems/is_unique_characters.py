class Solution:

    def is_unique_characters(self, input_string: str) -> bool:
        char_counts = dict()
        for char in input_string:
            if char in char_counts:
                return False
            char_counts[char] = 1
        return True


solution = Solution()
print(solution.is_unique_characters("hello"))

print(solution.is_unique_characters("abcdefg"))
