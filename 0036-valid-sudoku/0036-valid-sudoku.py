class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [[False] * 9 for _ in range(9)]
        col = [[False] * 9 for _ in range(9)]
        box = [[False] * 9 for _ in range(9)]

        for i in range(9):
            for j in range(9):
                c = board[i][j]
                if c != '.':
                    num = int(c) - 1
                    boxIdx = (i // 3) * 3 + j // 3
                    if row[i][num] or col[j][num] or box[boxIdx][num]:
                        return False
                    row[i][num] = True
                    col[j][num] = True
                    box[boxIdx][num] = True
        
        return True;