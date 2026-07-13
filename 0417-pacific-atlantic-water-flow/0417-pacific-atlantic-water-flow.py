class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])

        # 注入(x, y) 坐标列表，返回交集坐标列表
        def search(cells: List[Tuple[int, int]]) -> Set[Tuple[int, int]]:
            def dfs(i: int, j: int) -> None:
                if (i, j) in visited:  # 避免重复访问，避免反复横跳无限递归
                    return

                visited.add((i, j))  # 标记 (i,j) 已访问
                for x, y in (i, j - 1), (i, j + 1), (i - 1, j), (i + 1, j):
                    if 0 <= x < m and 0 <= y < n and heights[x][y] >= heights[i][j]:  # 往高处走
                        dfs(x, y)

            visited = set()
            for i, j in cells:
                dfs(i, j)
            return visited


        # 1.建立遍历的起点列表
        pacific = [(0, j) for j in range(n)] + [(i, 0) for i in range(1, m)]
        atlantic = [(m - 1, j) for j in range(n)] + [(i, n - 1) for i in range(m - 1)]
        # 2.递归搜索返回交集即为答案
        return list(search(pacific) & search(atlantic))
