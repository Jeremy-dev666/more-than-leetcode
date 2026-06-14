class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        ans = 0
        num = x
        while num > 0:
            ans = ans * 10 + num % 10
            num //= 10
        return ans == x