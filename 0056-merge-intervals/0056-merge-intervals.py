class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        ans = []
        prev = intervals[0]

        for cur in intervals[1:]:
            if cur[0] <= prev[1]:
                prev[1] = max(cur[1], prev[1])
            else:
                ans.append(prev)
                prev = cur

        ans.append(prev)
        return ans