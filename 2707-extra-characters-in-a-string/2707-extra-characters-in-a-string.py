# 字典树优化子串查询
class TrieNode:
    __slots__ = 'son', 'end'

    def __init__(self):
        self.son = {}
        self.end = False


class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        # 构建字典树
        root = TrieNode()
        for w in dictionary:
            cur = root
            for c in w[::-1]:
                if c not in cur.son:
                    cur.son[c] = TrieNode()
                cur = cur.son[c]
            cur.end = True

        # dp[i] 表示前i个字符的最小添加字符数量
        n = len(s)
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = dp[i - 1] + 1
            cur = root
            for j in range(i - 1, -1, -1):
                c = s[j]
                if c not in cur.son:
                    break
                cur = cur.son[c]
                
                if cur.end and dp[j] < dp[i]:
                    dp[i] = dp[j]

        return dp[n]