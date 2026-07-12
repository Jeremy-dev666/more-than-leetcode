class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        events = []
        for num, fr, to in trips:
            events.append((fr, num))
            events.append((to, -num))
        events.sort()

        total = 0
        for pos, num in events:
            total += num
            if total > capacity:
                return False
        return True
            