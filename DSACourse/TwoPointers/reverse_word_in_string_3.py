class Solution:
    def reverseWords(self, s: str) -> str:
        char_list = list(s)
        n = len(s)

        def reverse_word(start: int, end: int) -> None:
            while start < end:
                char_list[start], char_list[end] = char_list[end], char_list[start]
                start += 1
                end -= 1

        start = 0
        for end in range(n):
            if char_list[end] == " ":
                reverse_word(start=start, end=end - 1)
                start = end + 1
        reverse_word(start=start, end=n - 1)
        
        return ''.join(char_list)


sol = Solution()
print(sol.reverseWords("Let's take LeetCode contest"))
