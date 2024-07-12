class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        seen = set()

        for char in sentence:
            seen.add(char)

        return len(seen) == 26


sol = Solution()
print(sol.checkIfPangram("leetcode"))
