class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        f_max = f_min = ans = nums[0]
        for i in range(1, n):
            x = nums[i]
            new_max = max(x, f_max * x, f_min * x)
            new_min = min(x, f_max * x, f_min * x)
            f_max, f_min = new_max, new_min
            ans = max(ans, f_max)
        return ans