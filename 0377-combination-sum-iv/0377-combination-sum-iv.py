class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        n = len(nums)
        # 前k个物品能凑出target的方案数
        dp = [0] * (target + 1)
        dp[0] = 1

        for i in range(target + 1):
            for num in nums:
                if i >= num:
                    dp[i] += dp[i - num]

        return dp[target]