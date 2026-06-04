class Solution:
    def maximumCoins(self, coins: List[List[int]], k: int) -> int:
        def window(A):
            A.sort()
            ans = cur = j = 0
            for i in range(len(A)):
                cur += (A[i][1] - A[i][0] + 1) * A[i][2]
                # 减去刚刚累加过的区间但现在已经完全不在窗口内的
                while A[j][1] < A[i][1] - k + 1:
                    cur -= (A[j][1] - A[j][0] + 1) * A[j][2]
                    j += 1
                # 减去刚刚累加过与窗口范围部分不交叠的区间，但也可能不存在
                not_in = max(0, A[i][1] - k + 1 - A[j][0]) * A[j][2]
                # 更新答案
                ans = max(ans, cur - not_in)
        
            return ans
        
        # 因为window函数计算的是区间长度，所以l, r不需要担心负数，可以取反镜像
        return max(window(coins), window([[-r, -l, w] for l, r, w in coins]))