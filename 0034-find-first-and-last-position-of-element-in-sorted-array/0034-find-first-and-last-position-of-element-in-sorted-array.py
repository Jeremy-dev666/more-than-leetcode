class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        if n == 0:
            return [-1, -1]

        l, r = 0, n
        ans = [-1, -1]

        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid
        ans[0] = -1 if l == n or nums[l] != target else l

        l, r = 0, n
        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] <= target:
                l = mid + 1
            else:
                r = mid
        ans[1] = -1 if l == 0 or nums[l - 1] != target else l - 1

        return ans