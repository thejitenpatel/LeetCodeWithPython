class Solution:
    def numTrees(self, n: int) -> int:
        if n == 1:
            return 1
        
        dp = [0] * (n+1)
        dp[0], dp[1] = 1, 1

        for nodes in range(2, n + 1):
            total = 0
            for root in range(1, nodes + 1):
                left = dp[root - 1]
                right = dp[nodes - root]
                total += left * right
            dp[nodes] = total

        return dp[n]


solution = Solution()
print(solution.numTrees(n=1))
