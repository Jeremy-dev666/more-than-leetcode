class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n
        # 找到0下界
        while l < r:
            mid = (l + r) // 2
            if nums[mid] >= 0:
                r = mid
            else:
                l = mid + 1
        neg = l
        # 找到0上界
        l, r = 0, n
        while l < r:
            mid = (l + r) // 2
            if nums[mid] <= 0:
                l = mid + 1
            else:
                r = mid
        pos = n - l
        return max(pos, neg)
