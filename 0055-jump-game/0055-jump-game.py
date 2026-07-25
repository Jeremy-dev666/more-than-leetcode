class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True

        end = nums[0]
        for i in range(1, len(nums)):
            if i <= end:
                end = max(end, nums[i] + i)
                if end >= len(nums) - 1:
                    return True
            else:
                return False