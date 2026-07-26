class Solution:
    def myPow(self, x: float, n: int) -> float:
        # 处理负指数：x^(-n) = (1/x)^n
        if n < 0:
            x = 1 / x
            n = -n

        ans = 1.0
        while n != 0:
            if n & 1:
                ans *= x
            x *= x
            n >>= 1
        
        return ans