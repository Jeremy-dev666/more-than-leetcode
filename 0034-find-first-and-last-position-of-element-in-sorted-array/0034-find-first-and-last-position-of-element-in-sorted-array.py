class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # 二分找上界和下界问题
        n = len(nums)
        if n == 0:
            return [-1, -1]

        left, right = 0, n

        # 找上界
        while left < right:
            mid = left + (right - left) // 2
            if target < nums[mid]:
                right = mid
            else:
                left = mid + 1
        right_index = left - 1

        # 找上界
        left, right = 0, left
        while left < right:
            mid = left + (right - left) // 2
            if target > nums[mid]:
                left = mid + 1
            else:
                right = mid
        left_index = left
        
        if right_index < 0 or left_index >= n:
            return [-1, -1]
        if nums[left_index] != target or nums[right_index] != target:
            return [-1, -1]

        return [left_index, right_index]