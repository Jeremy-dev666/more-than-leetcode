class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = nums[0]
        t = 1
        for i in range(1, len(nums)):
            if nums[i] == c:
                t += 1
            else:
                t -= 1
                if t == 0:
                    c = nums[i]
                    t = 1
        return c