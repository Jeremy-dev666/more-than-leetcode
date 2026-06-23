class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        l, r = 0, len(height) - 1
        while l < r:
            lh, rh = height[l], height[r]
            max_area = max(max_area, min(lh, rh) * (r - l))
            if lh <= rh:
                l += 1
            else:
                r -= 1
        return max_area