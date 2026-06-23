class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        ans = 0
        for k in s:
            if k - 1 not in s:
                step = 1
                while k + step in s:
                    step += 1
                ans = max(ans, step)

        return ans