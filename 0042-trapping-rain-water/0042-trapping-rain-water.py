class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        l_max = r_max = 0
        ans = 0

        while left < right:
            l_max = max(l_max, height[left])
            r_max = max(r_max, height[right])
            if l_max <= r_max:
                ans += l_max - height[left]
                left += 1
            else:
                ans += r_max - height[right]
                right -= 1
        return ans