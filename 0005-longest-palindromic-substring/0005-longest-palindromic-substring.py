class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        n = len(s)
        if n <= 1:
            return s

        # dp[i][j] 表示当前子串[i, j]能否成为回文串
        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True

        start = 0
        max_len = 1

        # 对于动态规划过程中的遍历方向：
        # 看指针的依赖方向，比如这道题 dp[i][j] 依赖于 dp[i + 1][j - 1] 的结果
        # 也就是i指针依赖更大的索引，j指针依赖更小的索引
        # 所以i倒序遍历，j正序遍历
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    if j - i == 1:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]
                else:
                    dp[i][j] = False

                if dp[i][j] and (j - i + 1) > max_len:
                    max_len = j - i + 1
                    start = i

        return s[start: start + max_len]

