class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # enumerate 1 - max
        left, right = 1, max(piles)
        while left < right:
            k = (right + left) // 2
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / k)

            if hours <= h:
                right = k
            else:
                left = k + 1
        return right