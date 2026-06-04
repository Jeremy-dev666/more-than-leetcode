class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        if n <= 2:
            return True
        arr = nums.copy()
        for i in range(1, n):
            if nums[i] < nums[i - 1]:
                left = nums[:i]
                right = nums[i:]
                arr = right + left
                break
        for i in range(1, n):
            if arr[i] < arr[i - 1]:
                return False
        return True

                    