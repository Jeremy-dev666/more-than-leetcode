class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)
        while l < r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > nums[l]:
                if target >= nums[l] and target < nums[mid]:
                    r = mid
                else:
                    l = mid + 1
            else:
                if target <= nums[-1] and target > nums[mid]:
                    l = mid + 1
                else:
                    r = mid
        return -1
