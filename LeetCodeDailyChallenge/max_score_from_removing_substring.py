class Solution:

    def maximumGain(self, s: str, x: int, y: int) -> int:
        total_points = 0
        s = list(s)

        if x > y:
            # Remove "ab" first (higher points), then "ba"
            total_points += self.remove_substring(s, "ab", x)
            total_points += self.remove_substring(s, "ba", y)
        else:
            # Remove "ba" first (higher or equal points), then "ab"
            total_points += self.remove_substring(s, "ba", y)
            total_points += self.remove_substring(s, "ab", x)

        return total_points

    def remove_substring(
        self, input_string, target_substring, points_per_removal
    ):
        total_points = 0
        write_index = 0

        # Iterate through the string
        for read_index in range(0, len(input_string)):
            # Add the current character
            input_string[write_index] = input_string[read_index]
            write_index += 1

            # Check if we've written at least two characters and
            # they match the target substring
            if (
                write_index > 1
                and input_string[write_index - 2] == target_substring[0]
                and input_string[write_index - 1] == target_substring[1]
            ):
                write_index -= 2
                total_points += points_per_removal

        # Trim the list to remove any leftover characters
        del input_string[write_index:]

        return total_points

sol = Solution()
print(sol.maximumGain(s="cdbcbbaaabab", x=4, y=5))
