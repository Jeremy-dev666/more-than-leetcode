class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        # dp[i] 的定义：如果游戏只剩下 stoneValue[i:] 这些石子，且现在轮到某个人先手，这个人用最优策略走完剩下的所有回合后，他的总分减去对手总分，最多能是多少。

        n = len(stoneValue)
        dp = [0] * (n + 3)

        for i in range(n - 1, -1, -1):
            comp = float('-inf')
            turn_score = 0
            # 1 - 3个石子三轮情况，每一轮计算一次最大值
            for k in range(1, 4):
                if i + k - 1 < n:
                    turn_score += stoneValue[i + k - 1]
                    # turn_score - dp[i + k] 表示两个玩家比分查值
                    comp = max(comp, turn_score - dp[i + k])
            dp[i] = comp


        if dp[0] > 0:
            return 'Alice'
        elif dp[0] < 0:
            return 'Bob'
        else:
            return 'Tie'