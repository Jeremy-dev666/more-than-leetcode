class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 0:
            return 0
        
        # 初始状态（第 0 天之前）
        held = float('-inf')   # 不可能持有股票
        sold = float('-inf')   # 不可能刚卖出
        reset = 0              # 空仓，利润为 0
        
        for price in prices:
            # 必须用旧值同时更新，避免相互覆盖
            prev_held, prev_sold, prev_reset = held, sold, reset
            
            held = max(prev_held, prev_reset - price)   # 继续持有 or 今天买入
            sold = prev_held + price                     # 今天卖出
            reset = max(prev_reset, prev_sold)            # 保持空仓 or 冷冻期结束
        
        return max(sold, reset)