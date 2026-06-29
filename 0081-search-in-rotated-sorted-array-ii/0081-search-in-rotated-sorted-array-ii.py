class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums)
        while l < r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return True
            if nums[l] == nums[mid] and nums[mid] == nums[r]:
                l += 1
                r -= 1
            elif nums[mid] <= nums[r - 1]:
                if target > nums[mid] and target <= nums[r - 1]:
                    l = mid + 1
                else:
                    r = mid
            else:
                if target >= nums[l] and target < nums[mid]:
                    r = mid
                else:
                    l = mid + 1

        return False