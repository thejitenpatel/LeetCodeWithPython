class Solution:

    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""

        gcd_len = self.gcd(len(str1), len(str2))

        return str1[:gcd_len]

    def gcd(self, a: int, b: int) -> int:
        while b:
            a, b = b, a % b
        return a


sol = Solution()
sol.gcdOfStrings("LEET", "CODE")
