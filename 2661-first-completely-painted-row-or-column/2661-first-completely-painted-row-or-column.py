from collections import defaultdict

class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        
        # 记录每个数字在矩阵中的位置
        index_map = {}
        for i in range(m):
            for j in range(n):
                index_map[mat[i][j]] = (i, j)
        
        row_cnt = defaultdict(int)
        col_cnt = defaultdict(int)
        
        for idx, num in enumerate(arr):
            r, c = index_map[num]
            row_cnt[r] += 1
            col_cnt[c] += 1
            # 某行全涂完：该行计数 == 列数
            # 某列全涂完：该列计数 == 行数
            if row_cnt[r] == n or col_cnt[c] == m:
                return idx
        
        return -1