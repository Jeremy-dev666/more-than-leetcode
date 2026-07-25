class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        # four baselines
        top, btm, left, right = 0, m - 1, 0, n - 1

        ans = []
        while top <= btm and left <= right:
            for i in range(left, right + 1):
                ans.append(matrix[top][i])
            top += 1

            for i in range(top, btm + 1):
                ans.append(matrix[i][right])
            right -= 1

            if top <= btm:
                for i in range(right, left - 1, -1):
                    ans.append(matrix[btm][i])
                btm -= 1
            
            if left <= right:
                for i in range(btm, top - 1, -1):
                    ans.append(matrix[i][left])
                left += 1
                
        return ans