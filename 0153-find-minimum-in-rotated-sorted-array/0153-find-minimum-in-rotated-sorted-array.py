class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        left, right = 0, n
        while left < right:
            mid = left + (right - left) // 2
            num = nums[mid]
            if num > nums[-1]:
                left = mid + 1
            else:
                right = mid

        return nums[left]