"""
Given an encoded string, return its decoded string.

The encoding rule is : k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid
there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].

The test cases are generated so that the length of the output will never exceed 105.


Example 1:

Input: s = "3[a]2[bc]"
Output: "aaabcbc"
Example 2:

Input: s = "3[a2[c]]"
Output: "accaccacc"
Example 3:

Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"

Constraints:

1 <= s.length <= 30
s consists of lowercase English letters, digits, and square brackets '[]'.
s is guaranteed to be a valid input.
All the integers in s are in the range[1, 300].
"""


class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        current_string = ""
        k = 0

        for char in s:
            if char.isdigit():
                k = k * 10 + int(char)
            elif char == '[':
                stack.append((current_string, k))
                current_string = ""
                k = 0
            elif char == ']':
                prev_string, prev_k = stack.pop()
                current_string = prev_string + current_string * prev_k
            else:
                current_string += char

        return current_string
        # def decode(index):
        #     result = ""
        #     k = 0
        #     while index < len(s):
        #         char = s[index]
        #         if char.isdigit():
        #             k = k * 10 + int(char)
        #         elif char == '[':
        #             substr, index = decode(index + 1)
        #             result += k * substr
        #             k = 0
        #         elif char == ']':
        #             return result, index
        #         else:
        #             result += char
        #         index += 1
        #     return result

        # return decode(0)


sol = Solution()
print(sol.decodeString("2[abc]3[cd]ef"))
