class Solution:
    def maximumCoins(self, coins: List[List[int]], k: int) -> int:
        def window(A):
            A.sort()
            cur = j = ans = 0
            for i in range(len(A)):
                cur += (A[i][1] - A[i][0] + 1) * A[i][2]
                while A[i][1] - A[j][1] + 1 > k:
                    cur -= (A[j][1] - A[j][0] + 1) * A[j][2]
                    j += 1
                not_in = max(0, A[i][1] - k + 1 - A[j][0]) * A[j][2]
                ans = max(ans, cur - not_in)

            return ans
        # 对齐右端点或者左端点
        return max(window(coins), window([[-r, -l, w] for l , r, w in coins]))
