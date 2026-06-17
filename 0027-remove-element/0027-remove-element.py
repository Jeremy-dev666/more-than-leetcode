class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            while left < right and nums[left] == val:
                self.swap(nums, left, right)
                right -= 1
            left += 1
        cnt = 0
        for num in nums:
            if num == val:
                break
            cnt += 1
        return cnt

    def swap(self, nums, left, right):
        tmp = nums[left]
        nums[left] = nums[right]
        nums[right] = tmp