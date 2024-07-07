from typing import List


class Solution:
    def validStrings(self, n: int) -> List[str]:
        outs = []

        def f(x):
            if len(x) == n:
                outs.append(''.join(x))
                return
            x.append('1')
            f(x)
            x.pop()
            if len(x) == 0 or x[-1] == '1':
                x.append('0')
                f(x)
                x.pop()

        f([])
        return outs
        """
        outs = []

        def f(x):
            if len(x) == n:
                outs.append(''.join(x))
                return
            x.append('1')
            f(x)
            x.pop()
            if len(x) == 0 or x[-1] == '1':
                x.append('0')
                f(x)
                x.pop()

        f([])
        return outs
        """
        # def backtrack(current_string):
        #     if len(current_string) == n:
        #         result.append(current_string)
        #         return

        #     backtrack(current_string + "1")

        #     if not current_string or current_string[-1] != "0":
        #         backtrack(current_string + "0")

        # result = []
        # backtrack("")
        # return result


sol = Solution()
print(sol.validStrings(n=3))
