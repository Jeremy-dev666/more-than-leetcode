class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left, right = 0, n
        while left < right:
            mid = left + (right - left) // 2
            # 1.命中
            if nums[mid] == target:
                return mid
            # 2.mid左侧有序
            elif nums[mid] >= nums[left]:
                if target >= nums[left] and target < nums[mid]:
                    right = mid
                else:
                    left = mid + 1
            # 3.mid右侧有序
            else:
                if target <= nums[right - 1] and target > nums[mid]:
                    left = mid + 1
                else:
                    right = mid
        return -1