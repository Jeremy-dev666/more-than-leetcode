class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        ans = []
        idx, n = 0, len(intervals)

        # 左侧完全不重叠区间加入结果集
        while idx < n and newInterval[0] > intervals[idx][1]:
            ans.append(intervals[idx])
            idx += 1

        # 合并有交集的区间
        while idx < n and newInterval[1] >= intervals[idx][0]:
            newInterval[0] = min(newInterval[0], intervals[idx][0])
            newInterval[1] = max(newInterval[1], intervals[idx][1])
            idx += 1
        ans.append(newInterval)

        # 右侧完全不重叠区间加入结果集        
        while idx < n:
            ans.append(intervals[idx])
            idx += 1

        return ans