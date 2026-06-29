class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 1, x
        while l <= r:
            mid = (l + r) // 2
            mid2 = mid * mid
            if mid2 == x:
                return mid
            elif mid2 < x:
                l = mid + 1
            else:
                r = mid - 1
        return l - 1