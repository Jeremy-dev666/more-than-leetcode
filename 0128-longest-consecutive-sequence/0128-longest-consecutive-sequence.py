class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        ans = 0
        for num in nums_set:
            if num - 1 not in nums_set:
                cur_len = 1
                while num + cur_len in nums_set:
                    cur_len += 1
                ans = max(ans, cur_len)
        return ans