class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.m, self.n = len(board), len(board[0])
        if not self.valid(board, word):
            return False

        for row in range(self.m):
            for col in range(self.n):
                ch = board[row][col]
                if ch == word[0]:
                    if self.backtrack(board, word, row, col, 0):
                        return True

        return False

    def backtrack(self, board, word, row, col, index) -> bool:
        if index == len(word):
            return True
        if row < 0 or row >= self.m or col < 0 or col >= self.n:
            return False
        tmp = board[row][col]
        if tmp != word[index]:
            return False
        board[row][col] = "$"
        found = (
            self.backtrack(board, word, row - 1, col, index + 1) 
            or self.backtrack(board, word, row + 1, col, index + 1) 
            or self.backtrack(board, word, row, col - 1, index + 1) 
            or self.backtrack(board, word, row, col + 1, index + 1)
        )
        board[row][col] = tmp
        return found
        
    def valid(self, board, word) -> bool:
        cnt = {}
        for row in range(self.m):
            for col in range(self.n):
                ch = board[row][col]
                cnt[ch] = cnt.get(ch, 0) + 1
        for c in word:
            if c not in cnt or cnt[c] == 0:
                return False
            cnt[c] -= 1
        return True