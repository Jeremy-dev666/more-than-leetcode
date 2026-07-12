from collections import Counter

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        # 优化1：统计 board 中字符频率，若 word 需求超过 board 拥有量，直接返回 False
        board_count = Counter(c for row in board for c in row)
        word_count = Counter(word)
        for ch, cnt in word_count.items():
            if board_count[ch] < cnt:
                return False

        # 优化2：如果 word 尾字符在 board 中出现次数比首字符少，反转 word，从更稀有的一端开始搜索
        if board_count[word[0]] > board_count[word[-1]]:
            word = word[::-1]

        def dfs(i, j, k):
            if not (0 <= i < rows and 0 <= j < cols) or board[i][j] != word[k]:
                return False
            if k == len(word) - 1:
                return True

            tmp, board[i][j] = board[i][j], '#'
            # 优化3：用方向数组代替四次硬编码调用
            for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                if dfs(i + di, j + dj, k + 1):
                    board[i][j] = tmp
                    return True
            board[i][j] = tmp
            return False

        for i in range(rows):
            for j in range(cols):
                if dfs(i, j, 0):
                    return True
        return False