class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = "aeiou"
        max_vowels = 0
        count = 0
        for i in range(k):
            if s[i] in vowels:
                count += 1
        max_vowels = count

        for i in range(k, len(s)):
            if s[i] in vowels:
                count += 1
            if s[i - k] in vowels:
                count -= 1
            max_vowels = max(max_vowels, count)

        return max_vowels


sol = Solution()
print(sol.maxVowels(s="abciiidef", k=3))
