class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = right = 0
        n = len(nums)
        cntZero = ans = 0

        while right < n:
            if nums[right] == 0:
                cntZero += 1
            while left <= right and cntZero > k:
                if nums[left] == 0:
                    cntZero -= 1
                left += 1
            ans = max(ans, right - left + 1)
            right += 1

        return ans