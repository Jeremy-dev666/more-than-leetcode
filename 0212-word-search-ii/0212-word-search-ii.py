class TrieNode:
    __slots__ = 'son', 'word'

    def __init__(self):
        self.son = {}
        self.word = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        # 构建字典树
        root = TrieNode()
        for w in words:
            cur = root
            for c in w:
                if c not in cur.son:
                    cur.son[c] = TrieNode()
                cur = cur.son[c]
            cur.word = w


        ans = []
        m, n = len(board), len(board[0])    
        
        def dfs(i, j, cur_node):
            if not (0 <= i < m and 0 <= j < n):
                return
            
            c = board[i][j]
            if c == '$' or c not in cur_node.son:
                return

            cur_node = cur_node.son[c]
            if cur_node.word:
                ans.append(cur_node.word)
                cur_node.word = None

            board[i][j] = '$'
            dfs(i+1, j, cur_node)
            dfs(i-1, j, cur_node)
            dfs(i, j+1, cur_node)
            dfs(i, j-1, cur_node)
            board[i][j] = c

        for i in range(m):
            for j in range(n):
                dfs(i, j, root)
        return ans