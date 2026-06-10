import heapq

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        # 端点加楼栋索引并排序为扫描做准备
        edges = []
        for i, (left, right, height) in enumerate(buildings):
            edges.append((left, i))
            edges.append((right, i))
        edges.sort()

        # 扫描线
        idx = 0
        n = len(edges)
        live = [(0, float('inf'))]
        ans = []

        while idx < n:
            x = edges[idx][0]
            # 查询x位置有哪些楼栋端点
            while idx < n and edges[idx][0] == x:
                buildingIdx = edges[idx][1]
                left, right, height = buildings[buildingIdx]
                # 如果当前是左端点，表示楼栋开始进入视野
                # 入堆高度，右端点信息用于懒删除
                if left == x:
                    heapq.heappush(live, (-height, right))
                idx += 1

            # 懒删除不在视野内的楼栋
            while live[0][1] <= x:
                heapq.heappop(live)
            
            max_height = -live[0][0]

            # 比如[0, 2, 3] 和 [2, 5, 3] 两个楼栋就不需要重复记录
            if not ans or ans[-1][1] != max_height:
                ans.append([x, max_height])

        return ans