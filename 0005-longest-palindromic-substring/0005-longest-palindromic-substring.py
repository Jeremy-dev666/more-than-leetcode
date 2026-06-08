class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 1:
            return s

        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
        start = 0
        max_len = 1

        for length in range(2, n + 1):
            for i in range(0, n - length + 1):
                j = i + length - 1
                if s[i] == s[j]:
                    if length <= 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]
                else:
                    dp[i][j] = False

                if dp[i][j] and length > max_len:
                    max_len = length
                    start = i
        
        return s[start: start + max_len]
