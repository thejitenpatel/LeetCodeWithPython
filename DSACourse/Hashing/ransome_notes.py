from collections import Counter, defaultdict


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        letters = Counter(magazine)
        # ransome_counts = Counter(ransomNote)
        # print(counts - ransome_counts)
        for char in ransomNote:
            if letters[char] <= 0:
                return False
            letters[char] -= 1
        return True


sol = Solution()
print(sol.canConstruct(ransomNote="aa", magazine="aab"))
