class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l, r = 0, len(nums) - 1
        ans = [0] * len(nums)
        p = len(nums) - 1
        while l <= r:
            a = nums[l] * nums[l]
            b = nums[r] * nums[r]
            if a < b:
                ans[p] = b
                r -= 1
            else:
                ans[p] = a
                l += 1
            p -= 1
        return ans