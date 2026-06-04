class Solution:
    def reverse(self, x: int) -> int:
        is_neg = False
        if x < 0:
            is_neg = True
            x *= -1
        
        num = 0
        while x > 0:
            digit = x % 10
            x //= 10
            if (num > (2 ** 31 - 1) // 10) or (num == (2 ** 31 - 1) // 10 and digit > 7):
                return 0
            num = num * 10 + digit

        return num if not is_neg else -num