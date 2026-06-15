class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)

        # 斜对称轴交换
        for i in range(m):
            for j in range(i):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = tmp

        # 左右对称交换
        for i in range(m):
            for j in range(m // 2):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[i][m - j - 1]
                matrix[i][m - j - 1] = tmp
        

