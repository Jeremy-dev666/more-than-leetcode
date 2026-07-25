class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 开一个数组标记哪一行或哪一列至少有一个零
        m, n = len(matrix), len(matrix[0])
        zero_flag = [0] * (m + n)
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    zero_flag[i] = 1
                    zero_flag[m + j] = 1

        
        for i in range(m + n):
            if zero_flag[i] and i < m:
                for k in range(n):
                    matrix[i][k] = 0
            if zero_flag[i] and i >= m:
                for k in range(m):
                    matrix[k][i - m] = 0
        