class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left, right = 0, n

        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid

            # 查mid落在哪段数组里
            if nums[mid] >= nums[left]:
                # 确认target是落在mid所指的哪个区间数组内
                if target >= nums[left] and target < nums[mid]:
                    right = mid
                else:
                    left = mid + 1
            else:
                if target <= nums[right - 1] and target > nums[mid]:
                    left = mid + 1
                else:
                    right = mid

        return -1

