class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        lst = rst = 0
        ans = 0
        while l <= r:
            lst = max(lst, height[l])
            rst = max(rst, height[r])
            if lst <= rst:
                ans += lst - height[l]
                l += 1
            else:
                ans += rst - height[r]
                r -= 1

        return ans
