class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.ans = []
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i < 2 or dp[i + 1][j - 1]):
                    dp[i][j] = True

        self.backtrack(s, dp, 0, [])
        return self.ans

    def backtrack(self, s, dp, left, path) -> None:
        n = len(s)
        if left == n:
            self.ans.append(list(path))
            return
        
        for right in range(left, n):
            if not dp[left][right]:
                continue
            path.append(s[left:right+1])
            self.backtrack(s, dp, right + 1, path)
            path.pop()