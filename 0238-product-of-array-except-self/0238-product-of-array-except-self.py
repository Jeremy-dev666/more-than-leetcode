class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        p = [0] * (n + 1)
        p[0] = 1
        for i in range(1, n + 1):
            p[i] = nums[i - 1] * p[i - 1]

        s = 1
        for j in range(n, 0, -1):
            p[j] = p[j - 1] * s
            s *= nums[j - 1]

        return p[1:]