from collections import defaultdict
from typing import List


class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        lossers_count = [-1] * 100001

        for winner, lossers in matches:
            if lossers_count[winner] == -1:
                lossers_count[winner] = 0
            if lossers_count[lossers] == -1:
                lossers_count[lossers] = 0
            else:
                lossers_count[lossers] += 1
        
        answer = [[], []]
        for i in range(100001):
            if lossers_count[i] == 0:
                answer[0].append(i)
            elif lossers_count[i] == 1:
                answer[1].append(i)

        return answer


sol = Solution()
print(sol.findWinners(matches=[[1, 3], [2, 3], [3, 6], [
      5, 6], [5, 7], [4, 5], [4, 8], [4, 9], [10, 4], [10, 9]]))
