class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # speed == [1, max:piles[i]]
        l, r = 1, max(piles)
        while l <= r:
            mid = (l + r) // 2
            t = self.cntTime(mid, piles)
            if t > h:
                l = mid + 1
            else:
                r = mid - 1
        return l

    def cntTime(self, speed, piles):
        t = 0
        for p in piles:
            t += (p + speed - 1) // speed
        return t