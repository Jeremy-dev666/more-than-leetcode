class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        # 将区间按照首元素升序排序
        intervals.sort(key=lambda x:x[0])

        # 取第一组区间初始化，从第二组区间开始遍历
        n = len(intervals)
        prev = intervals[0]
        ans = []

        for cur in intervals[1:]:
            # 验证当前区间能否与上一区间合并
            # 若能则继续合并，不能则将上一区间加入结果集
            if cur[0] <= prev[1]:
                prev[1] = max(prev[1], cur[1])
            else:
                ans.append(prev)
                prev = cur
        
        ans.append(prev)
        return ans
                