class Solution:
    def numDecodings(self, s: str) -> int:

        n = len(s)
        s = " " + s  # 增加一个哨兵
        dp = [0] * (n + 1)  # 前i个位置解码的最大数量
        dp[0] = 1

        for i in range(1, n + 1):
            num1 = int(s[i])
            num2 = int(s[i-1:i+1])
            if 1 <= num1 <= 9:
                dp[i] = dp[i - 1]
            if 10 <= num2 <= 26:
                dp[i] += dp[i - 2]

        return dp[n]
        