from collections import defaultdict
from typing import List


class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        losses_count = [-1] * 100001

        for winner, losser in matches:
            if losses_count[winner] == -1:
                losses_count[winner] = 0
            if losses_count[losser] == -1:
                losses_count[losser] = 1
            else:
                losses_count[losser] += 1
        
        answer = [[], []]
        for i in range(100001):
            if losses_count[i] == 0:
                answer[0].append(i)
            elif losses_count[i] == 1:
                answer[1].append(i)

        return answer


sol = Solution()
print(sol.findWinners(matches=[[1, 3], [2, 3], [3, 6], [
      5, 6], [5, 7], [4, 5], [4, 8], [4, 9], [10, 4], [10, 9]]))
