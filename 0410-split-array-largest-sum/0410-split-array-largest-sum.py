class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l, r = max(nums), sum(nums)
        while l < r:
            mid = (l + r) // 2
            if self.canSplit(mid, nums, k):
                r = mid
            else:
                l = mid + 1
        return l
    
    def canSplit(self, target, nums, k):
        cnt = 1
        total = 0
        for num in nums:
            if total + num > target:
                total = 0
                cnt += 1
            total += num
        return cnt <= k