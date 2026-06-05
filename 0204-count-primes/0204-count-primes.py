class Solution:
    def countPrimes(self, n: int) -> int:
        isPrime = [True] * n
        # 枚举范围
        for i in range(2, int(n ** 0.5) + 1):
            if isPrime[i]:
                # 排除所有非素数
                for j in range(i * i, n, i):
                    isPrime[j] = False

        ans = 0
        for i in range(2, n):
            if isPrime[i]: 
                ans += 1

        return ans