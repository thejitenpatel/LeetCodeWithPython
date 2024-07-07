from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
        """
        if len(s) != len(t):
            return False

        count_s = {}
        count_t = {}

        for char in s:
            if char in count_s:
                count_s[char] += 1
            else:
                count_s[char] = 1

        for char in t:
            if char in count_t:
                count_t[char] += 1
            else:
                count_t[char] = 1

        return count_s == count_t
        """


sol = Solution()
print(sol.isAnagram(s="rat", t="cat"))
