class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[1], nums[0])

        def rob_circle(start, end):
            n = end - start + 1
            dp = [0] * n
            dp[0] = nums[start]
            dp[1] = max(nums[start], nums[start + 1])
            for i in range(2, n):
                dp[i] = max(dp[i - 1], dp[i - 2] + nums[start + i])
            return dp[n - 1]

        x_rob_1 = rob_circle(1, n - 1)
        x_rob_2 = rob_circle(0, n - 2)
        return max(x_rob_1, x_rob_2)
