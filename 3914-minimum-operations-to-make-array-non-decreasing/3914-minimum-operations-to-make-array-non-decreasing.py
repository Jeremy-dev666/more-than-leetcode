class Solution:
    def minOperations(self, nums: list[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0

        prev_val = nums[0]   # a[i-1]
        prev_need = 0        # need[i-1]
        ans = 0

        for i in range(1, n):
            if nums[i] < prev_val:
                need = prev_val - nums[i]  # a[i] = prev_val
            else:
                prev_val = nums[i]         # a[i] = nums[i]
                need = 0

            if need > prev_need:
                ans += need - prev_need

            prev_need = need

        return ans