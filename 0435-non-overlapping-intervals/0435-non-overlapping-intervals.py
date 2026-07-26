class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[0])
        prev = intervals[0]
        n = len(intervals)
        ans = 0

        for cur in intervals[1:]:
            if cur[0] < prev[1]:
                ans += 1
                # 把较大端点的区间去除掉，这样能保证后面少重叠
                prev[1] = min(prev[1], cur[1])
            else:
                prev = cur

        return ans