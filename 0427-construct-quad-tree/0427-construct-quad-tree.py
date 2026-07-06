class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        m, n = len(grid), len(grid[0])
        
        # 构建二维前缀和数组，prefix_sum[i][j] 表示 grid[0..i-1][0..j-1] 这个子矩阵内 1 的个数
        # 这样就能 O(1) 求出任意子矩形区域内 1 的总数，从而判断该区域是否为"纯色"（全0或全1）
        prefix_sum = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                prefix_sum[i + 1][j + 1] = (
                    prefix_sum[i + 1][j] + prefix_sum[i][j + 1] 
                    - prefix_sum[i][j] + grid[i][j]
                )

        # dfs(startx, starty, endx, endy)：
        # 处理左上角为 (startx, starty)，右下角为 (endx, endy) 的子网格（左闭右开区间）
        def dfs(startx, starty, endx, endy):
            # 利用前缀和公式，计算当前子矩形区域内 1 的个数
            diff = (
                prefix_sum[endx][endy] - prefix_sum[endx][starty] 
                - prefix_sum[startx][endy] + prefix_sum[startx][starty]
            )
            
            # 情况一：区域内 1 的个数为 0，说明全是 0 -> val=False, isLeaf=True
            if diff == 0:
                return Node(False, True, None, None, None, None)
            
            # 情况二：区域内 1 的个数等于区域总格子数，说明全是 1 -> val=True, isLeaf=True
            elif diff == (endx - startx) * (endy - starty):
                return Node(True, True, None, None, None, None)
            
            # 情况三：0 和 1 都存在，说明不是纯色 -> 非叶子节点，需要切成四份递归处理
            else:
                hx = (startx + endx) // 2  # 横向中点
                hy = (starty + endy) // 2  # 纵向中点
                return Node(
                    True,   # val 在非叶子节点时任意赋值即可
                    False,  # isLeaf = False
                    dfs(startx, starty, hx, hy),   # 左上
                    dfs(startx, hy, hx, endy),     # 右上
                    dfs(hx, starty, endx, hy),     # 左下
                    dfs(hx, hy, endx, endy)        # 右下
                )
        
        return dfs(0, 0, m, n)