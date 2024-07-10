from typing import List


class Solution:
    def minOperations(self, logs: List[str]) -> int:
        count = 0

        for operation in logs:
            if operation == "../":
                count = max(0, count - 1)
            elif operation != "./":
                count += 1
        return count


sol = Solution()
print(sol.minOperations(["d1/", "d2/", "../", "d21/", "./"]))
