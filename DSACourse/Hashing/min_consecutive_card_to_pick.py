from collections import defaultdict
from typing import List


class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        dic = defaultdict(int)
        ans = float("inf")
        for i in range(len(cards)):
            if cards[i] in dic:
                ans = min(ans, i - dic[cards[i]] + 1)

            dic[cards[i]] = i

        return ans if ans < float("inf") else -1


sol = Solution()
print(sol.minimumCardPickup([3, 4, 2, 3, 4, 4, 7]))
