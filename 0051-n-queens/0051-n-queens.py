class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        queens = [-1] * n
        ans = []
        self.backtrack(queens, ans, n, 0)
        return ans

    def backtrack(self, queens: List[int], ans: List[List[str]], n: int, row: int) -> None:
        if row == n:
            ans.append(self.build(queens))
            return

        for col in range(n):
            if self.isValid(queens, row, col):
                queens[row] = col
                self.backtrack(queens, ans, n, row + 1)
                queens[row] = -1

    def isValid(self, queens: List[int], row: int, col: int) -> bool:
        for i in range(row):
            if queens[i] == col:
                return False
            if abs(row - i) == abs(col - queens[i]):
                return False
        return True

    def build(self, queens: List[int]) -> List[str]:
        board = []
        n = len(queens)
        for i in range(n):
            row_arr = ['.'] * n
            row_arr[queens[i]] = 'Q'
            board.append(''.join(row_arr))
        return board
