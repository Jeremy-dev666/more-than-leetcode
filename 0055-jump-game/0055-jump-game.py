class Solution:
    def canJump(self, nums: List[int]) -> bool:
        window = 0
        for i in range(len(nums)):
            if i <= window:
                extend = i + nums[i]
                window = max(window, extend)
                if window >= len(nums) - 1:
                    return True
            else:
                return False