class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if len(intervals) == 0:
            return True
        
        intervals.sort(key=lambda x:x[0])
        prev = intervals[0]

        for cur in intervals[1:]:
            if cur[0] < prev[1]:
                return False
            else:
                prev = cur

        return True