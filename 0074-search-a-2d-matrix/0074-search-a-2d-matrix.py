class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix) * len(matrix[0])
        l, r = 0, n
        while l < r:
            mid = (l + r) // 2
            row = mid // len(matrix[0])
            col = mid % len(matrix[0])
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                l = mid + 1
            else:
                r = mid
        return False