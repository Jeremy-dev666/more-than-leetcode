from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.isWord = False

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        root = TrieNode()
        n = len(s)

        for word in wordDict:
            cur = root
            for c in word:
                if c not in cur.children:
                    cur.children[c] = TrieNode()
                cur = cur.children[c]
            cur.isWord = True

        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(1, n+1):
            # 当前k个元素能凑成单词，继续搜索
            if dp[i - 1]:
                cur = root
                # 遍历后续字符
                for j in range(i, n + 1):
                    if s[j - 1] not in cur.children:
                        break
                    cur = cur.children[s[j - 1]]
                    if cur.isWord:
                        dp[j] = True
        return dp[n]
