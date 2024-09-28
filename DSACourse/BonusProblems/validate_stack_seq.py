from typing import List


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        j = 0
        for i in pushed:
            stack.append(i)
            while stack and stack[-1] == popped[j]:
                stack.pop()
                j += 1

        return j == len(popped)


sol = Solution()
print(sol.validateStackSequences(
    pushed=[1, 2, 3, 4, 5], popped=[4, 5, 3, 2, 1]))
