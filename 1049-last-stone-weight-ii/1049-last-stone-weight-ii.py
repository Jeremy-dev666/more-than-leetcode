class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total = sum(stones)
        target = total // 2
        n = len(stones)
        dp = [[0] * (target + 1) for _ in range(n + 1)]

        # 对于每一件物品，考虑要不要放入到每一个不同容量背包中
        for i in range(1, n + 1):
            w = stones[i - 1]
            for j in range(1, target + 1):
                if j >= w:
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w] + w)
                else:
                    dp[i][j] = dp[i - 1][j]

        max_weight = dp[n][target]
        return total - 2 * max_weight
