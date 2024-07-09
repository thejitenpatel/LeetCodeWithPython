class Solution:
    def reverseWords(self, s: str) -> str:
        n = len(s)
        start = 0
        end = n - 1

        while start < n and s[start] == " ":
            start += 1

        while end >= 0 and s[end] == " ":
            end -= 1

        words = []
        i = start
        
        while i <= end:
            while i <= end and s[i] == " ":
                i += 1

            if i > end:
                break

            word_start = i

            while i <= end and s[i] != " ":
                i += 1

            word_end = i - 1

            words.append(s[word_start:word_end + 1])

        left, right = 0, len(words) - 1

        while left < right:
            words[left], words[right] = words[right], words[left]
            left += 1
            right -= 1

        result = ""

        for i in range(len(words)):
            result += words[i]
            if i < len(words) - 1:
                result += " "
                
        return result



sol = Solution()
print(sol.reverseWords("the sky is blue"))
