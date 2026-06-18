class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        end = cur_end = 0
        jumps = 0
        for i in range(n - 1):
            end = max(end, i + nums[i])
            if i == cur_end:
                jumps += 1
                cur_end = end
        return jumps