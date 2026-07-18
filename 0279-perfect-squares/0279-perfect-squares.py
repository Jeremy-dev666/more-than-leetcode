class Solution:
    def numSquares(self, n: int) -> int:
        # 首先找到打点的范围 [0, sqrt(n) + 1), 计算出平方数列表
        sqr_list = [i**2 for i in range(0, int(math.sqrt(n)) + 1)]

        # 容量为k时的最少平方数数量
        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        for i in range(1, n + 1):
            for sqr in sqr_list:
                if i >= sqr:
                    dp[i] = min(dp[i], dp[i - sqr] + 1)
        
        return dp[n]

