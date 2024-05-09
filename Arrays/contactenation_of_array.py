from typing import List

print("Hellow")


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums + nums


sol = Solution()
print(sol.getConcatenation([1, 2, 3]))
