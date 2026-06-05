class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        left = right = 0
        ans = inf
        sum = 0
        while right < n:
            sum += nums[right]
            while left <= right and sum >= target:
                ans = min(ans, right - left + 1)
                sum -= nums[left]
                left += 1
            right += 1
        return ans if ans != inf else 0