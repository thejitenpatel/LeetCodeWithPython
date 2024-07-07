class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        k %= len(s)
        return s[k:] + s[:k]
    
sol = Solution()
print(sol.getEncryptedString(s="dart", k=3))
