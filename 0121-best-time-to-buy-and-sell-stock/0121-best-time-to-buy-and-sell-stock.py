class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        hold = float('inf')
        for p in prices:
            ans = max(ans, p - hold)
            hold = min(hold, p)
        return ans