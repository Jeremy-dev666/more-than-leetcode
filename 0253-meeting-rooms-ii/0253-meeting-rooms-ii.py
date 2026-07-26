class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        events = []
        for start, end in intervals:
            events.append((start, 1))
            events.append((end, -1))

        events.sort(key=lambda x:(x[0], x[1]))
        rooms = ans = 0

        for time, val in events:
            rooms += val
            ans = max(ans, rooms)

        return ans