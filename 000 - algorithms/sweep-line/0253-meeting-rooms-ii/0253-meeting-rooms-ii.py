class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        events = []
        for start, end in intervals:
            events.append((start, 1))
            events.append((end, -1))

        events.sort(key=lambda x: (x[0], x[1]))
        rooms = 0
        ans = 0
        for time, d in events:
            rooms += d
            ans = max(ans, rooms)
        
        return ans