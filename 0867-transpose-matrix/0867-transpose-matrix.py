class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        ans = [[0] * m for _ in range(n)]

        for r, row in enumerate(matrix):
            for c, num in enumerate(row):
                ans[c][r] = num
        return ans
