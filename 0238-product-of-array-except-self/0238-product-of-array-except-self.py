class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        for i in range(1, len(nums)):
            prefix[i] = prefix[i - 1] * nums[i - 1]
        suffix = 1
        for j in range(len(nums)-1, -1, -1):
            prefix[j] = suffix * prefix[j]
            suffix *= nums[j]
        return prefix