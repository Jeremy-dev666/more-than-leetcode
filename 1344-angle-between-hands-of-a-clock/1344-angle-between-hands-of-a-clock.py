class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        M = 6
        H = 30
        a1 = minutes * M
        a2 = (hour % 12 + minutes / 60) * H
        diff = abs(a2 - a1)
        return min(diff, 360 - diff)