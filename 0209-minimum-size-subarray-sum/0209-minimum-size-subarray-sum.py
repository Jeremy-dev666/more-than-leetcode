class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans = float('inf')
        l = r = sum = 0
        while r < len(nums):
            sum += nums[r]
            while sum >= target:
                ans = min(ans, r - l + 1)
                sum -= nums[l]
                l += 1
            r += 1
        return 0 if ans == float('inf') else ans