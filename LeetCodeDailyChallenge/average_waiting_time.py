from typing import List


class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        next_idle_time = 0
        next_wait_time = 0

        for customer in customers:
            next_idle_time = max(customer[0], next_idle_time) + customer[1]
            next_wait_time += next_idle_time - customer[0]

        return next_wait_time / len(customers)


sol = Solution()
print(sol.averageWaitingTime([[1, 2], [2, 5], [4, 3]]))
