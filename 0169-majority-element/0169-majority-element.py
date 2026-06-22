class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = nums[0]
        t = 0
        for k in nums:
            if t == 0:
                c = k
            t = t + 1 if k == c else t - 1
        return c