import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        # 按开始时间排序
        intervals.sort(key=lambda x: x[0])

        # 最小堆，存每个房间当前会议的结束时间
        heap = []

        for start, end in intervals:
            if heap and heap[0] <= start:
                # 最早结束的房间已空闲，复用它
                heapq.heapreplace(heap, end)
            else:
                # 没有空闲房间，新开一间
                heapq.heappush(heap, end)

        return len(heap)