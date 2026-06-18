class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        diff = float("inf")
        for i in range(n):
            a = nums[i]
            l, r = i + 1, n - 1
            while l < r:
                b, c = nums[l], nums[r]
                total = a + b + c
                if abs(target - total) < abs(diff):
                    diff = target - total
                if total < target:
                    l += 1
                else:
                    r -= 1

            if diff == 0:
                break
        return target - diff
