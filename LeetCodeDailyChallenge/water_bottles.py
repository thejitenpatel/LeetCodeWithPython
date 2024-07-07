class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans, tmp = numBottles, numBottles
        while tmp >= numExchange:
            new = tmp // numExchange
            tmp = tmp % numExchange + new
            ans += new
        return ans


sol = Solution()
print(sol.numWaterBottles(9, 3))
