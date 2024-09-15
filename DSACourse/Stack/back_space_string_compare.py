class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def build(s: str):
            stack = []
            for c in s:
                if c != "#":
                    stack.append(c)
                elif stack:
                    stack.pop()
            return "".join(stack)
        return build(s) == build(t)


sol = Solution()
print(sol.backspaceCompare(s="ab#c", t="ad#c"))
